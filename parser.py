import pandas as pd

def load_and_clean_data(file_path):

    # Import files
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.strip()

    # Clean date
    df['Date'] = pd.to_datetime(df['Posted Transactions Date'], format='%d/%m/%Y', errors='coerce', dayfirst=True)
    df = df.dropna(subset=['Posted Transactions Date']) 

    # Clean amount
    df['Debit Amount'] = df['Debit Amount'].replace(',', '', regex=True)
    df['Debit Amount'] = pd.to_numeric(df['Debit Amount'], errors='coerce')

    return df

def filter_by_date(df, start_date, end_date):
    mask = (df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))
    return df.loc[mask]
