def analyze_budget(df, income):
    advice = []

    # Total spend by category
    category_totals = df.groupby('Predicted Label')['Debit Amount'].sum()

    # 1. Dining out > 20% of income
    dining_total = category_totals.get('Food & Coffee', 0)
    if dining_total > 0.2 * income:
        advice.append(f"⚠️ Dining spend is €{dining_total:.2f}, which is over 20% of your income. Consider cutting back.")

    # 2. Detect subscriptions
    subscription_keywords = ['netflix', 'spotify', 'amazon prime', 'openai', 'chill insurance']
    subscriptions = df[df['Description1'].str.lower().str.contains('|'.join(subscription_keywords))]
    if subscriptions.empty:
        advice.append("✅ No obvious subscriptions detected.")
    else:
        unused = subscriptions.groupby('Description1')['Debit Amount'].count().reset_index()
        unused = unused[unused['Debit Amount'] <= 1]

    # Extract simplified names
    simplified_names = subscriptions['Description1'].str.extract(r'(?i)(netflix|spotify|amazon prime|openai|chill insurance)', expand=False)
    clean_names = simplified_names.dropna().unique()
    advice.append("🔍 Found subscriptions worth consider cancelling:\n" + ", ".join(clean_names))

    # 3. Detect fuel costs
    fuel_total = category_totals.get('Fuel', 0)
    if fuel_total > 0.1 * income:
        advice.append(f"⛽️ Fuel expenses are high (€{fuel_total:.2f}). Consider carpooling or optimizing trips.")

    # 4. Check gaming and entertainment costs
    entertainment_keywords = ['game', 'steam', 'xbox', 'playstation', 'epic', 'mondello']
    entertainment = df[df['Description1'].str.lower().str.contains('|'.join(entertainment_keywords))]
    if not entertainment.empty and entertainment['Debit Amount'].sum() > 0.05 * income:
        advice.append("🎮 High spend detected on games/entertainment. Might want to cut back.")
 
    # 5.Coffee shops - (too many caramel mochiato grandes or whaterever)
    coffee_keywords = ['starbucks', 'costa', 'insomnia', 'café', 'get go coffee']
    coffees = df[df['Description1'].str.lower().str.contains('|'.join(coffee_keywords))]
    if len(coffees) > 10:
        advice.append(f"☕️ You've visited coffee shops {len(coffees)} times. That adds up!")

    # 6.Check for other or unusual shops
    dupes = df['Description1'].value_counts()
    suspect_merchants = dupes[dupes > 10]

    if suspect_merchants.empty:
        advice.append("✅ No unusual shops detected.")
    else:
        simplified_names_shops = subscriptions['Description1'].str.extract(r'(?i)(amazon|amzn|ebay|ikea|harvey norman|deciem|home store|woodies|pepco|h&m|zara|paypal|belles|smyths|blanchardst|halfords|local|adverts|doyles|blanch|organised|liffey|the range|holland|pull and bear|boots|nutbutter|dbrand|heatons|navan|haggard|perfectpla|bulbs direct|yeti|tenoo)', expand=False)
        clean_names_shops = simplified_names_shops.dropna().unique()
        advice.append("🧐 Multiple frequent transactions from these merchants — double check they're valid:\n" + ", ".join(clean_names_shops))

    # 7. What about savings?
    saving_keywords = ['savings', 'deposit']
    savings = df[df['Description1'].str.lower().str.contains('|'.join(saving_keywords))]
    if savings.empty:
        advice.append("💰 No savings activity found. Consider setting aside at least 10% monthly.")

    # High spending overall
    total_spend = df['Debit Amount'].sum()
    if total_spend > income:
        advice.append(f"💸 You're spending €{total_spend:.2f}, which is more than your income (€{income:.2f}).")
    else:
        advice.append(f"✅ Spending is under control: €{total_spend:.2f} vs income €{income:.2f}.")

    return advice
