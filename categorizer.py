def categorize(description):   
    desc = description.lower()

    categories = {
        "Groceries": ["aldi", "lidl", "tesco", "supervalu", "dunnes", "mr price", "day to day", "penneys", "home bargains"],
        "Fuel": ["applegreen", "maxol", "circle k", "inver", "naas oil", "esso"],
        "Food & Coffee": ["costa", "mcdonalds", "apache", "cafe", "restaurant", "jump juice", "starbucks", "butlers", "pizza", "supermacs", "donut", "burger king", "insomnia"],
        "Vapes": ["vape", "ecig", "electronic cig"],
        "Services": ["netflix", "spotify", "google", "youtube", "facebook", "openai"],
        "Direct Debits": ["d/d", "panda", "pure telecom", "premium credit", "electric ireland", "aib", "naps loan", "chill insurance", "eflow"],
        "Shopping": ["amazon", "ebay", "ikea", "harvey norman", "deciem", "home store", "woodies", "pepco", "h&m", "zara"],
        "Transfers": ["revolut", "transfer", "*mobi", "xfr", "*inet"],
        "Pets": ["pet", "zoo", "petstop", "pets at home", "petmania"],
        "Entertainment": ["cinema", "odeon", "mondello", "tickets", "park", "tibradde", "regatta", "weev"],
        "Rent": ["rent"],
        "Pharmacy/Health": ["pharma", "chemist", "lifephar", "holland and barrett", "clinic"],
        "Bars & Alcohol": ["bar", "off licence", "brewery", "pub", "club", "fosters"],
        "Gifts & Misc": ["tiger", "perfume", "flowers", "gift", "souvenir", "smith's", "choice", "eason"],
        "Transport & Car": ["ncts", "car", "garage", "tyres", "autocare", "motor", "chargepoint", "ionity", "motor tax", "eflow"],
        "Accommodation": ["hotel", "b&b"],
    }

    for category, keywords in categories.items():
        if any(k in desc for k in keywords):
            return category

    return "Other"
