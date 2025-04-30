import pandas as pd
from categorizer import categorize

def load_and_clean_data(df):

    # Import files
    df.columns = df.columns.str.strip()

    # Ensure necessary columns exist
    required_columns = ['Description1', 'Debit Amount', 'Credit Amount', 'Posted Currency', 'Transaction Type', 'Posted Transactions Date']
    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        print(f"Warning: Missing columns: {', '.join(missing_columns)}")

    # Clean 'Description1' by removing leading/trailing spaces and converting to lowercase
    df['Description1'] = df['Description1'].str.strip().str.lower()

    # Handle missing values
    df.dropna(subset=['Description1'], inplace=True)  # Drop rows with missing descriptions

    df['Debit Amount'] = pd.to_numeric(df['Debit Amount'], errors='coerce').fillna(0)
    df['Credit Amount'] = pd.to_numeric(df['Credit Amount'], errors='coerce').fillna(0)

    # Convert 'Transaction Type' and 'Posted Currency' to categorical types
    df['Transaction Type'] = df['Transaction Type'].astype('category')
    df['Posted Currency'] = df['Posted Currency'].astype('category')
    
    # Convert 'Posted Transactions Date' to usable date
    df['Date'] = pd.to_datetime(df['Posted Transactions Date'], format='%d/%m/%Y', errors='coerce', dayfirst=True)
    
    df["Label"] = df["Description1"].astype(str).apply(categorize)

    df[["Description1", "Label", "Debit Amount"]].to_csv("test2.csv", index=False)

    return df

def filter_by_date(df, start_date, end_date):
    mask = (df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))
    return df.loc[mask]
