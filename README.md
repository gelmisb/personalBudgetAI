# PersonalBudgetAI

## Overview
PersonalBudgetAI is a machine learning-powered tool for personal budgeting. It automatically categorizes transaction data using various machine learning models, helping users analyze their spending habits.

## Features
- Automatically categorizes transactions from CSV data
- Uses machine learning models (e.g., Naive Bayes, Decision Tree, XGBoost, etc.)
- Provides accuracy evaluation and model performance metrics
- Helps visualize and analyze transaction trends

## Requirements
- Python 3.6+
- pandas
- scikit-learn
- xgboost
- matplotlib (for visualizations)

To install the required libraries, use:
	`pip install -r requirements.txt`


## Usage

1. Prepare your transaction data in a CSV file with columns: `Description1`, `Amount`, and `Label`.
2. Run the main script to load and process the data:
    ```bash
    python main.py
    ```
3. The script will categorize the transactions based on the trained model, providing predictions and analysis.

## Example Usage
```python
from personalBudgetAI import categorize, train_model

# Categorize a single transaction description
category = categorize("Bought groceries at Tesco")
print(f"Category: {category}")

# Train a new model using labeled transaction data
train_model("transaction_data.csv")
