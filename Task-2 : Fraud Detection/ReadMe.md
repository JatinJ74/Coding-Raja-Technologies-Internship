# Fraud Detection in Financial Transactions

## Overview

This project aims to develop a machine learning model to detect fraudulent transactions in a financial dataset. The dataset contains transaction records with features such as transaction type, amount, balance, and whether the transaction is fraudulent or not.

## Steps

### 1. Data Collection
- The dataset used in this project is obtained from Kaggle.
- It includes features like `step`, `type`, `amount`, `nameOrig`, `oldbalanceOrg`, `newbalanceOrig`, `nameDest`, `oldbalanceDest`, `newbalanceDest`, `isFraud`, and `isFlaggedFraud`.

### 2. Data Preprocessing
- Cleaned the data and handled missing values.
- Balanced the dataset to address class imbalance if needed.
- Used `StandardScaler` from scikit-learn to scale the numerical features.
- Computed the Variance Inflation Factor (VIF) for each feature using `variance_inflation_factor` from `statsmodels.stats.outliers_influence` to detect multicollinearity.
- Applied `LabelEncoder` from scikit-learn to encode categorical features into numerical values.

### 3. Train-Test Split
- Split the dataset into training and testing sets using `train_test_split` from scikit-learn.

### 4. Model Training
- Trained a Random Forest classifier using `RandomForestClassifier` from scikit-learn.
- Alternatively, trained a Decision Tree classifier using `DecisionTreeClassifier` from scikit-learn.

### 5. Model Evaluation
- Evaluated the model's performance using metrics like accuracy, precision, recall, and F1-score.
- Generated a classification report using `classification_report` from scikit-learn.
- Plotted a confusion matrix using `confusion_matrix` from scikit-learn.
- Displayed the confusion matrix using `ConfusionMatrixDisplay` from scikit-learn.

### 6. Visualization
- Used `seaborn` and `matplotlib.pyplot` for data visualization.

## Tech Stack
- Python
- Data manipulation libraries (e.g., pandas)
- Machine learning libraries (e.g., scikit-learn)
- Statistical libraries (e.g., statsmodels)
- Visualization libraries (e.g., seaborn, matplotlib)

## Usage
- Clone the repository.
- Install the required dependencies.
- Run the Jupyter Notebook file containing the code.

## Results

The models achieved high accuracy scores in detecting fraudulent transactions. Additionally, the classification reports provided detailed insights into the precision, recall, and F1-score of the models. The confusion matrices visualized the performance of the models in classifying fraudulent and non-fraudulent transactions.

## Conclusion

The developed machine learning model, along with the implemented preventive measures, provide a robust framework for detecting and preventing fraudulent activities in financial transactions. By leveraging advanced data preprocessing techniques, model training, and evaluation, organizations can enhance their security measures and protect their financial assets effectively.
