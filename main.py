import pandas as pd

from parser import load_and_clean_data
from categorizer import categorize
from advisor import analyze_budget

def main():
    df = load_and_clean_data('test1.csv')

    df['Category'] = df['Description1'].apply(categorize)
    df['Week'] = df['Date'].dt.to_period('W').apply(lambda r: r.start_time)  # Gives Monday of the week
    df['Month'] = df['Date'].dt.to_period('M')

    print("\n--- Categorized Preview ---")
    print(df[['Description1', 'Category', 'Debit Amount']].head(30))

    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df['Week'] = df['Date'].dt.isocalendar().week

    weekly = df.groupby('Week')['Debit Amount'].sum().reset_index()
    print(weekly)

    # Assuming you've loaded and categorized your `df` already
    monthly_income = 3000  # Adjust as needed
    advice = analyze_budget(df, monthly_income)

    print("\n--- Budget Insights ---")
    for item in advice:
        print(item)

if __name__ == '__main__':
    main()
