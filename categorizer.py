def categorize(description):   
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

    df['Category'] = df['Description1'].apply(categorize)

    print(df['Debit Amount'].isna().sum())

    df['Date'] = pd.to_datetime(df['Posted Transactions Date'])  
    df['Month'] = df['Date'].dt.to_period('M')

    monthly_summary = df.groupby(['Month', 'Category'])['Debit Amount'].sum().unstack().fillna(0)