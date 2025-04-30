import streamlit as st
import altair as alt

from processing import predict_categories_and_generate_report
from parser import load_and_clean_data
from advisor import analyze_budget
from predict_next_month import predict_next_month_spending

import pandas as pd

st.title("Personal Budget AI")

st.write("Hi, I'm Finny - your financial buddy!\n Just upload your docs below.")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    if not {"Description1", "Label"}.issubset(df.columns):
        st.success('The uploaded CSV is being processed!', icon="✅")
        df = load_and_clean_data(df)
        
    # Run prediction engine
    result_df, report, prediction_string = predict_categories_and_generate_report(df)

    # Show prediction result
    st.subheader(prediction_string + ", huh?")
    st.write("So it seems like you have been spending most of your money on " + prediction_string)
    st.write("See how I knew that? Want to see what else I know about your shopping habbits?")

    st.divider()

    with st.expander("Spending by Category"):
        st.subheader("📊 Spending Breakdown by Category")

        # Use 'Predicted Label' if present, else 'Label'
        category_column = 'Predicted Label' if 'Predicted Label' in result_df.columns else 'Label'



        if category_column in result_df.columns and 'Debit Amount' in result_df.columns:
            category_spend = result_df.groupby(category_column)['Debit Amount'].sum().sort_values(ascending=False)
            
            st.bar_chart(category_spend)
            st.write("Total spend per category:")
            st.dataframe(category_spend)
        else:
            st.warning("Categories or debit amounts missing from dataset.")


    st.divider()
    with st.expander("Spending Overview"):
        # Prompt user for fallback date if needed
        if 'Posted Transactions Date' not in df.columns:
            st.warning("📅 'Posted Transactions Date' column is missing. Please enter a date to use for all entries.")
            fallback_date = st.date_input("Select a fallback date for transactions", value=pd.to_datetime("today").date())
        else:
            fallback_date = None
        # Predict spending and plot
        try:
            predicted_spend, monthly_totals = predict_next_month_spending(df, fallback_date)
            st.subheader("📊 Predicted Monthly Spending Overview")
            # st.line_chart(monthly_totals.set_index('YearMonth'))

            chart = alt.Chart(monthly_totals).mark_line(point=True).encode(
            x=alt.X('YearMonth:N', title='Month'),
            y=alt.Y('Debit Amount:Q', title='Spending (€)'),
            tooltip=['YearMonth', 'Debit Amount']
        ).properties(title='Spending by Month') 
            st.altair_chart(chart, use_container_width=True)
            st.success(f"📈 Predicted spend for next month: €{predicted_spend:.2f}")
        except ValueError as e:
            st.error(str(e))

    st.divider()

    with st.expander("Budget Advisor Insights"):
        st.write("## 💡 Budget Advisor Insights")

        income = st.number_input("Enter your monthly income (€):", min_value=0, step=100)

        if income > 0:
            advice = analyze_budget(result_df, income)
            for point in advice:
                st.markdown(f"- {point}")
        else:
            st.info("Please enter your income above to receive tailored financial advice.")

    st.divider()

    # Create a collapsible section
    with st.expander("Nerd stats"):
        # Show classification report
        st.subheader("Classification Report - MLPClassifier (Neural Network model)")
        st.dataframe(report)

