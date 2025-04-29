import streamlit as st
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


    predicted_spend, monthly_totals = predict_next_month_spending(df)
    st.subheader("📈 Predicted Next Month's Spend")
    st.write(f"Estimated spending based on recent trends: **€{predicted_spend:.2f}**")
    st.line_chart(monthly_totals.set_index('YearMonth'))


    # # Extract predicted label
    # predicted_label = prediction_string.replace("Predicted Category: ", "")

    # # Let user override
    # st.subheader("Adjust Predicted Category")
    # label_options = result_df["Label"].unique().tolist()
    # new_label = st.selectbox("Choose a new category if prediction is incorrect:", label_options, index=label_options.index(predicted_label))

    # if new_label != predicted_label:
    #     st.success(f"Category changed to: {new_label}")
    # else:
    #     st.info("You kept the predicted category.")

    st.divider()

    st.write("## 💡 Budget Advisor Insights")

    income = st.number_input("Enter your monthly income (€):", min_value=0, step=100)

    if income > 0:
        advice = analyze_budget(result_df, income)
        for point in advice:
            st.markdown(f"- {point}")
    else:
        st.info("Please enter your income above to receive tailored financial advice.")

    # Show classification report
    st.subheader("Classification Report")
    st.text(report)
