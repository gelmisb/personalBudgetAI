import pandas as pd

def predict_next_month_spending(df):
    # Convert to datetime
    df['Posted Transactions Date'] = pd.to_datetime(df['Posted Transactions Date'])

    # Filter only debits (expenses)
    df_expenses = df[df['Debit Amount'] > 0].copy()

    # Group by year and month
    df_expenses['YearMonth'] = df_expenses['Posted Transactions Date'].dt.to_period('M')
    monthly_totals = df_expenses.groupby('YearMonth')['Debit Amount'].sum().reset_index()
    monthly_totals['YearMonth'] = monthly_totals['YearMonth'].astype(str)

    # Simple prediction: average of last 3 months
    if len(monthly_totals) >= 3:
        predicted_spend = monthly_totals['Debit Amount'].tail(3).mean()
    else:
        predicted_spend = monthly_totals['Debit Amount'].mean()

    return predicted_spend, monthly_totals
