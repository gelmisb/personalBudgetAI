import pandas as pd

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    # Clean date
    df['Date'] = pd.to_datetime(df['Posted Transactions Date'], errors='coerce')

    # Clean amount
    df['Debit Amount'] = df['Debit Amount'].replace(',', '', regex=True)
    df['Debit Amount'] = pd.to_numeric(df['Debit Amount'], errors='coerce')

    return df
