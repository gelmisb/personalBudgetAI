import pandas as pd
from datetime import datetime

from parser import load_and_clean_data, filter_by_date
from categorizer import categorize
from advisor import analyze_budget

def main():

    print("\n--- Welcome to personal budgeting services ---")
    print("\n--- Enter dates you would like to analyse (no date enetered will be replaced with today's date) ---\n")

    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")

    if not start or not end:
        today = datetime.today()
        start = today.replace(day=1)
        end = today

    df = load_and_clean_data('test1.csv')
    df = filter_by_date(df, start, end)

    df['Category'] = df['Description1'].apply(categorize)
    df['Week'] = df['Date'].dt.to_period('W').apply(lambda r: r.start_time)  
    df['Month'] = df['Date'].dt.to_period('M')

    print("\n--- Categorized Preview ---")
    print(df[['Description1', 'Category', 'Debit Amount']].head(30))

    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df['Week'] = df['Date'].dt.isocalendar().week

    weekly = df.groupby('Week')['Debit Amount'].sum().reset_index()
    print(weekly)

    monthly_income = 3000  # Adjust as needed
    advice = analyze_budget(df, monthly_income)

    print("\n--- Budget Insights ---")
    for item in advice:
        print(item)

if __name__ == '__main__':
    main()
