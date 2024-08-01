# 03-Introduction-to-Machine-Learning-Classification

## Basic Banking Classification

This repository contains a Python script for a basic banking classification model. The script is designed to predict whether a person will apply for a financial product based on various features.

## Dependencies

The script requires the following Python libraries:

- pandas
- sklearn
- xgboost
- pickle
- matplotlib
- numpy

## Data

The data used in this script is a cleaned banking dataset, which can be found [here](https://raw.githubusercontent.com/konradbachusz/AI-training/main/classification/data/bank_cleaned.csv).

## Usage

The script performs the following steps:

1. **Data Loading**: Loads the dataset from the provided URL.
2. **Data Preprocessing and Feature Engineering**: One-hot encodes categorical features and removes original features.
3. **Data Splitting**: Splits the data into training and testing sets.
4. **Model Training**: Trains a Logistic Regression model and an XGBoost model on the training data.
5. **Model Evaluation**: Evaluates the models' performance using accuracy, precision, recall, and AUC metrics. It also displays the confusion matrix and the AUC curve.
6. **Model Saving**: Saves the final XGBoost model to a pickle file.
7. **Model Loading**: Loads a pre-trained model from a pickle file.
8. **Prediction**: Makes predictions on new data and visualizes the prediction probabilities using a gauge chart.

You can run it in Google Colab via [this link](https://colab.research.google.com/gist/konradbachusz/f0117ef57bc7365a350046e69ebb00e6/basic_banking_classification.ipynb)

