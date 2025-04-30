import pandas as pd
import altair as alt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv('test2_good.csv')

# Clean any missing data
df.dropna(subset=['Description1', 'Label'], inplace=True)

# Split the data into features (X) and labels (y)
X = df['Description1']  # The transaction descriptions
y = df['Label']         # The labels (categories)

# Initialize LabelEncoder to convert string labels to numeric labels
label_encoder = LabelEncoder()

# Fit and transform the labels
y_encoded = label_encoder.fit_transform(y)

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

# Fit and transform the descriptions into a document-term matrix
X_tfidf = vectorizer.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y_encoded, test_size=0.2, random_state=42)

# Initialize MLPClassifier (Neural Network model)
model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Predict the categories for the test set
y_pred = model.predict(X_test)

# Convert the numeric predictions back to string labels
y_pred_labels = label_encoder.inverse_transform(y_pred)

# Evaluate the model
print("Classification Report:\n", classification_report(y_test, y_pred))

# Example: predicting a new transaction description
new_transaction = ["Bought groceries at Tesco"]
new_tfidf = vectorizer.transform(new_transaction)
prediction = model.predict(new_tfidf)

# Convert the numeric prediction back to the string label
new_prediction_label = label_encoder.inverse_transform(prediction)

print(f"Predicted Category: {new_prediction_label[0]}\n\n")

# Assuming you have the true labels `y_true` and predicted labels `y_pred_labels`
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, average='weighted', zero_division=1))
print("Recall:", recall_score(y_test, y_pred, average='weighted', zero_division=1))
print("F1-Score:", f1_score(y_test, y_pred, average='weighted', zero_division=1))

# Or if you're using classification_report, add zero_division parameter as well:
print("Classification Report:\n", classification_report(y_test, y_pred, zero_division=1))
