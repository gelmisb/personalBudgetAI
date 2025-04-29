from parser import load_and_clean_data
from categorizer import categorize

def main():
    df = load_and_clean_data('test.csv')
    df['Category'] = df['Description1'].apply(categorize)
    df['Month'] = df['Date'].dt.to_period('M')

    print("\n--- Spend by Category ---")
    print(df.groupby('Category')['Debit Amount'].sum().sort_values(ascending=False))

    print("\n--- Monthly Breakdown ---")
    monthly = df.groupby(['Month', 'Category'])['Debit Amount'].sum().unstack().fillna(0)
    print(monthly.round(2))

if __name__ == '__main__':
    main()
