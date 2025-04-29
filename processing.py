import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
import xgboost as xgb

df = pd.read_csv('test2_good.csv')

# Clean any missing data
df.dropna(subset=['Description1', 'Label'], inplace=True)

# Split the data 
X = df['Description1']  # The transaction descriptions
y = df['Label']         # The labels (categories)

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the descriptions into a document-term matrix
X_tfidf = vectorizer.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Initialize Naive Bayes classifier
model = MultinomialNB()

# Train the model
model.fit(X_train, y_train)

# Predict the categories for the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))

# Example: predicting a new transaction description
new_transaction = ["Bought groceries at Tesco"]
new_tfidf = vectorizer.transform(new_transaction)
prediction = model.predict(new_tfidf)

# Display the prediction for the new transaction
print(f"Predicted Category: {prediction[0]}\n\n")

# Calculate and print additional metrics for the test set
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted', zero_division=1))
print("Recall:", recall_score(y_test, y_pred, average='weighted', zero_division=1))
print("F1-Score:", f1_score(y_test, y_pred, average='weighted', zero_division=1))
