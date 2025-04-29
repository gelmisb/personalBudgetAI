import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('test2_good.csv')

# Clean any missing data
df.dropna(subset=['Description1', 'Label'], inplace=True)

# Split the data into features (X) and labels (y)
X = df['Description1']  # The transaction descriptions
y = df['Label']         # The labels (categories)

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the descriptions into a document-term matrix
X_tfidf = vectorizer.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

# Initialize Decision Tree classifier
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict the categories for the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Classification Report:\n", classification_report(y_test, y_pred))

# Example: predicting a new transaction description
new_transaction = ["Bought groceries at Tesco"]
new_tfidf = vectorizer.transform(new_transaction)
prediction = model.predict(new_tfidf)

print(f"Predicted Category: {prediction[0]}\n\n")

# Evaluate using accuracy, precision, recall, and F1-score
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted', zero_division=1))
print("Recall:", recall_score(y_test, y_pred, average='weighted', zero_division=1))
print("F1-Score:", f1_score(y_test, y_pred, average='weighted', zero_division=1))
