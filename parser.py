import pandas as pd

df = pd.read_csv('test.csv')

df.columns = df.columns.str.strip()
df['Debit Amount'] = df['Debit Amount'].replace(',', '', regex=True)
df['Debit Amount'] = pd.to_numeric(df['Debit Amount'], errors='coerce')