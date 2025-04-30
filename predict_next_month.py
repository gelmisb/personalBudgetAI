import pandas as pd

def predict_next_month_spending(df, fallback_date=None):
    # Check if the column is present
    if 'Posted Transactions Date' not in df.columns:
        if fallback_date is None:
            raise ValueError("❌ No 'Posted Transactions Date' column, and no fallback date provided.")
        df['Posted Transactions Date'] = pd.to_datetime(fallback_date)
    else:
        df['Posted Transactions Date'] = pd.to_datetime(df['Posted Transactions Date'], errors='coerce')
        if df['Posted Transactions Date'].isna().all():
            if fallback_date is None:
                raise ValueError("❌ 'Posted Transactions Date' exists but all values are invalid. Provide a fallback date.")
            df['Posted Transactions Date'] = pd.to_datetime(fallback_date)

    # Fill missing/invalid with fallback
    if fallback_date:
        df['Posted Transactions Date'].fillna(pd.to_datetime(fallback_date), inplace=True)

    # Filter expenses
    df_expenses = df[df['Debit Amount'] > 0].copy()

    # If all dates are the same fallback, simulate 3 months
    unique_dates = df_expenses['Posted Transactions Date'].dt.to_period('M').nunique()
    if unique_dates <= 1:
        df_expenses = df_expenses.reset_index(drop=True)
        month_offsets = df_expenses.index % 3
        df_expenses['Posted Transactions Date'] = df_expenses['Posted Transactions Date'] + month_offsets.map(lambda x: pd.DateOffset(months=x))

    df_expenses['YearMonth'] = df_expenses['Posted Transactions Date'].dt.to_period('M')
    monthly_totals = df_expenses.groupby('YearMonth')['Debit Amount'].sum().reset_index()
    monthly_totals['YearMonth'] = monthly_totals['YearMonth'].astype(str)

    # Prediction: avg of last 3 months
    if len(monthly_totals) >= 3:
        predicted_spend = monthly_totals['Debit Amount'].tail(3).mean()
    else:
        predicted_spend = monthly_totals['Debit Amount'].mean()

    return predicted_spend, monthly_totals
