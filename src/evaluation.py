#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import click
import pandas as pd
import pickle
import os
from sklearn.metrics import accuracy_score
from Modeling import split_x_y
from sklearn.metrics import f1_score, confusion_matrix
from sklearn.metrics import precision_score, recall_score


@click.command()
@click.option('--test-data', type=str, required=True, help="Path to test data") # data/processed
@click.option('--pipeline-from', type=str, required=True, help="Path where the fit model is saved") # results/models
@click.option('--results-to', type=str, required=True, help="Path to the results folder where all metrics are saved") #results/tables

def main(test_data, pipeline_from, results_to):

    test_df = pd.read_csv(os.path.join(test_data, "license_test.csv"))
    
    y_test = test_df["survival_status"]
    
    X_test_transformed = pd.read_csv(os.path.join(test_data, "scaled_test.csv"))
    X_test_transformed = X_test_transformed.to_numpy()
    
    
    with open(pipeline_from + "/lr_license_renewal_pipeline.pickle", 'rb') as f:
        license_fit = pickle.load(f)
    
    
    # Make predictions on the test set
    predictions = license_fit.predict(X_test_transformed)
    
    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy: {accuracy:.2f}")
    
    # Calculate F1 score
    f1 = f1_score(y_test, predictions)
    print(f"F1 Score: {f1:.2f}")
    
    # Calculate confusion matrix
    conf_matrix = confusion_matrix(y_test, predictions)
    conf_matrix_df = pd.DataFrame(conf_matrix, index=['Actual 0', 'Actual 1'], columns=['Predicted 0', 'Predicted 1'])
    conf_matrix_df.to_csv(results_to + "/confusion_matrix.csv", index=False)
    
    
    # Calculate precision
    precision = precision_score(y_test, predictions)
    print(f"Precision: {precision:.2f}")
    
    # Calculate recall
    recall = recall_score(y_test, predictions)
    print(f"Recall: {recall:.2f}")
    
    print("\n")
    print(conf_matrix_df.head())
    
    
    columns = ['Accuracy', 'F1_Score', 'Precision', 'Recall']
    values = [[round(accuracy,2), round(f1,2), round(precision,2), round(recall,2)]]
    
    test_results = pd.DataFrame(values, columns=columns)
    
    test_results.to_csv(results_to +"/test_scores.csv", index=False)

if __name__ == "__main__":
    main()