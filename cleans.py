import pandas as pd

def clean_dataset_otherwise(df):

    # Ensure necessary columns exist
    required_columns = ['Description1', 'Debit Amount', 'Credit Amount', 'Posted Currency', 'Transaction Type', 'Posted Transactions Date']
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        print(f"Warning: Missing columns: {', '.join(missing_columns)}")

    # Clean 'Description1' by removing leading/trailing spaces and converting to lowercase
    df['Description1'] = df['Description1'].str.strip().str.lower()

    # Handle missing values
    df.dropna(subset=['Description1'], inplace=True)  # Drop rows with missing descriptions

    # Fill missing numerical values with 0 for debit and credit amounts
    df['Debit Amount'].fillna(0, inplace=True)
    df['Credit Amount'].fillna(0, inplace=True)

    # Ensure 'Debit Amount' and 'Credit Amount' are numeric
    df['Debit Amount'] = pd.to_numeric(df['Debit Amount'], errors='coerce').fillna(0)
    df['Credit Amount'] = pd.to_numeric(df['Credit Amount'], errors='coerce').fillna(0)

    # Optionally, convert 'Transaction Type' and 'Posted Currency' to categorical types
    df['Transaction Type'] = df['Transaction Type'].astype('category')
    df['Posted Currency'] = df['Posted Currency'].astype('category')

    # We also need a date to predict future spending
    df['Posted Transactions Date'] = pd.to_datetime(df['Posted Transactions Date'])

    # Save cleaned data
    return df
