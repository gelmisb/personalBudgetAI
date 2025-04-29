import pandas as pd
# from parser import load_and_clean_data

def categorize(description):
    description = description.lower()
    
    categories = {
        "Groceries": ["aldi", "lidl", "tesco", "supervalu", "dunnes", "mr price", "penneys", "home bargains", "express", "super asia", "lituanica"],
        "Fuel": ["applegreen", "maxol", "circle k", "inver", "naas oil", "esso", "kiltale", "statoil", "obama"],
        "Food & Coffee": ["costa", "mcdonalds", "apache", "cafe", "restaurant", "jump juice", "starbucks", "butlers", "pizza", "supermacs", "donut", "burger king", "insomnia", "dodo", "coffee", "bobs", "pizz", "golden", "nichols", "krispy", "lady", "nya", "essencevault", "the art", "cola", "platterbyl", "wines", "bear market", "pelco"],
        "Vapes": ["vape", "ecig", "electronic cig", "souhans", "londis", "vip", "hale"],
        "Services": ["netflix", "spotify", "google", "youtube", "facebook", "openai", "facebk", "ring"],
        "Direct Debits": ["d/d", "panda", "pure telecom", "premium credit", "aib", "naps loan", "chill insurance", "eflow", "qtr", "virgin media", "ashbourne"],
        "Shopping": ["amazon", "amzn", "ebay", "ikea", "harvey norman", "deciem", "home store", "woodies", "pepco", "h&m", "zara", "paypal", "belles", "smyths", "blanchardst", "halfords", "local", "adverts", "doyles", "blanch", "organised", "liffey", "the range", "holland", "pull and bear", "boots", "nutbutter", "dbrand", "heatons", "navan", "haggard", "perfectpla", "bulbs direct", "yeti", "tenoo"],
        "Transfers": ["revolut", "transfer", "*mobi", "xfr", "*inet", "neringa"],
        "Pets": ["pet", "zoo", "petstop", "pets at home", "petmania"],
        "Entertainment": ["cinema", "odeon", "mondello", "tickets", "park", "tibradde", "regatta", "weev", "special", "whiteriver", "hobby", "sugarloaf", "fressnapf", "courtlough", "raw elements", "wicklow"],
        "Rent": ["rent"],
        "Pharmacy/Health": ["pharma", "chemist", "lifephar", "holland and barrett", "clinic", "conor", "maple", "revive"],
        "Bars & Alcohol": ["bar", "off licence", "brewery", "pub", "club", "fosters"],
        "Gifts & Misc": ["tiger", "perfume", "flowers", "gift", "souvenir", "smith's", "choice", "eason", "ups"],
        "Transport & Car": ["ncts", "car", "garage", "tyres", "autocare", "motor", "chargepoint", "ionity", "motor tax", "eflow", "asap", "chill", "smartpart", "m3", "m11", "northlink"],
        "Accommodation": ["hotel", "b&b"],
        "Savings": ["savings"],
        "Withdrawal": ["atm", "point cash", "withdrawal", "the square"],
        "Fishing": ["sportfins", "southside angl"],
        "Electricity": ["electric ireland"],
        "Heating (Oil)": ["home heat"], 
        "Small shops": ["day to day", "tom", "centra", "dealz", "crazy", "jl grocery", "glenbeigh", "spar", "clonee", "balbriggan", "selecta", "o shaughnessy", "fitzgerald", "fontique", "sheehans", "melo", "maunsells", "ballycommon", "rathnew"]
    }

    for category, keywords in categories.items():
        if any(keyword in description for keyword in keywords):
            return category
    return "Uncategorized"

# df = load_and_clean_data('test1.csv')
# print("Columns in CSV:", df.columns.tolist())

# df["Label"] = df["Description1"].astype(str).apply(categorize)

# df['Debit Amount'] = df['Debit Amount'].replace(',', '', regex=True)
# df['Debit Amount'] = pd.to_numeric(df['Debit Amount'], errors='coerce')

# df[["Description1", "Label", "Debit Amount"]].to_csv("test2.csv", index=False)

# print("✅ Labeled transactions saved to 'test2.csv'")
