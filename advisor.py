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

    # 3. High spending overall
    total_spend = df['Debit Amount'].sum()
    if total_spend > income:
        advice.append(f"💸 You're spending €{total_spend:.2f}, which is more than your income (€{income:.2f}).")
    else:
        advice.append(f"✅ Spending is under control: €{total_spend:.2f} vs income €{income:.2f}.")

    return advice
