from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from sklearn.neural_network import MLPClassifier
import pandas as pd


def predict_categories_and_generate_report(df):

    # Ensure required columns exist
    required_columns = {"Description1", "Label"}
    if not required_columns.issubset(df.columns):
        raise ValueError(f"CSV must contain the following columns: {required_columns}")

    # Drop missing or malformed rows
    df.dropna(subset=["Description1", "Label"], inplace=True)

    # Optional: remove empty or whitespace-only descriptions
    df = df[df["Description1"].str.strip() != ""]

    # Otherwise continue as usual
    df.dropna(subset=['Description1', 'Label'], inplace=True)
    
    X = df['Description1']
    y = df['Label']

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    vectorizer = TfidfVectorizer(stop_words='english')
    X_tfidf = vectorizer.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y_encoded, test_size=0.2, random_state=42)

    model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    report = classification_report(
        y_test,
        y_pred,
        labels=list(range(len(label_encoder.classes_))),
        target_names=label_encoder.classes_,
        zero_division=1
    )

    # Predict the label of a sample transaction
    new_transaction = ["Bought groceries at Tesco"]
    new_tfidf = vectorizer.transform(new_transaction)
    prediction = model.predict(new_tfidf)
    prediction_string = f"{label_encoder.inverse_transform(prediction)[0]}"

    # Optional: add predictions to a copy of the original df
    labeled_df = df.copy()
    labeled_df["Predicted Label"] = label_encoder.inverse_transform(model.predict(X_tfidf))
    

    return labeled_df, report, prediction_string
