import pandas as pd

df = pd.read_csv('test.csv')

# Lowercase all keywords upfront
groc = ["tesco", "aldi", "lidl", "lituanica", "dunnes", "express", "supervalu"]
services = ["google", "spotify", "netflix", "ring"]
dds = ["pure", "ashbourne", "gym", "virgin media", "panda"]
miscStores = ["tiger", "choice", "harvey", "red cow tyres", "grafton", "perfectpla", "revive"]
rent = ["rent"]
fuel = ["applegreen", "maxol"]
vapes = ["londis", "vape", "souhans"]
revolut = ["revolut"]
foodCoffee = ["costa", "eurolink", "mcdonalds", "jump juice", "central"]

def categorize(description):
    desc = description.lower()
    for x in groc:
        if x in desc:
            return "Groceries"
    for x in services:
        if x in desc:
            return "Services"
    for x in dds:
        if x in desc:
            return "Direct Debits"
    for x in miscStores:
        if x in desc:
            return "Miscellaneous Shops"
    for x in rent:
        if x in desc:
            return "Rent"
    for x in fuel:
        if x in desc:
            return "Fuel"
    for x in vapes:
        if x in desc:
            return "Vapes"
    for x in revolut:
        if x in desc:
            return "Revolut Transfers"
    for x in foodCoffee:
        if x in desc:
            return "Food & Coffee"
    return "Other"

df.columns = df.columns.str.strip()
df['Debit Amount'] = df['Debit Amount'].replace(',', '', regex=True)
df['Debit Amount'] = pd.to_numeric(df['Debit Amount'], errors='coerce')
df['Category'] = df['Description1'].apply(categorize)

# Optional: print result summary
# print(df.groupby("Category")["Debit Amount"].sum())
print(df['Debit Amount'].isna().sum())


df['Date'] = pd.to_datetime(df['Posted Transactions Date'])  # ensure proper datetime
df['Month'] = df['Date'].dt.to_period('M')

monthly_summary = df.groupby(['Month', 'Category'])['Debit Amount'].sum().unstack().fillna(0)
print(monthly_summary)
