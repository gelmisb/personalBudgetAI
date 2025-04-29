def analyze_budget(df, income):
    advice = []

    # Total spend by category
    category_totals = df.groupby('Category')['Debit Amount'].sum()

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
        if not unused.empty:
            advice.append("🔍 Found subscriptions with only 1 recent charge — consider cancelling:\n" +
                          "\n".join(unused['Description1'].values))

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
    if not suspect_merchants.empty:
        advice.append("🧐 Multiple frequent transactions from these merchants — double check they're valid:\n" +
                      "\n".join(suspect_merchants.index[:3]))

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
