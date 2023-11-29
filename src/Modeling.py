import numpy as np
import click
import pandas as pd
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.model_selection import cross_validate
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import FunctionTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import (
    OneHotEncoder,
    StandardScaler,
)
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import cross_validate
from sklearn.linear_model import LogisticRegression

def transform(df, word_features, categorical_features, numeric_features):
    """
    Transform and preprocess a DataFrame with different types of features.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the features to be transformed.
    - word_features (list of str): List of column names corresponding to text features in the DataFrame.
    - categorical_features (list of str): List of column names corresponding to categorical features in the DataFrame.
    - numeric_features (list of str): List of column names corresponding to numeric features in the DataFrame.

    Returns:
    - numpy.ndarray: The transformed array containing the preprocessed features.
    """
    
    # drop_features = ['Status', 'BusinessSubType', 'FOLDERYEAR', 'LicenceRSN', 'LicenceNumber', 'LicenceRevisionNumber',
    #     'BusinessName', 'BusinessTradeName', 'IssuedDate', 'ExpiredDate', 
    #     'Unit', 'UnitType', 'House', 'Street', 'ExtractDate', 'Geom', 'geo_point_2d']
    
    word_transformer = make_pipeline(
        SimpleImputer(strategy="most_frequent"),
        FunctionTransformer(np.reshape, kw_args={'newshape':-1}),
        CountVectorizer(binary=True)
    )

    categorical_transformer = make_pipeline(
        SimpleImputer(strategy="most_frequent"),
        OneHotEncoder(drop="if_binary", sparse_output=False, handle_unknown='ignore')
    )

    numeric_transformer = make_pipeline(
        SimpleImputer(strategy="median"),
        StandardScaler()
    )
    
    word_trans_arr = word_transformer.fit_transform(df[word_features])
    categorical_trans_arr = categorical_transformer.fit_transform(df[categorical_features])
    numeric_trans_arr = numeric_transformer.fit_transform(df[numeric_features])
    
    return np.hstack((word_trans_arr.toarray(), categorical_trans_arr, numeric_trans_arr))


def split_x_y(df, word_features, categorical_features, numeric_features):
    """
    Extracts features (X) and target variable (y) from a DataFrame.

    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing both features and the target variable.
    - word_features (list of str): List of column names corresponding to text features in the DataFrame.
    - categorical_features (list of str): List of column names corresponding to categorical features in the DataFrame.
    - numeric_features (list of str): List of column names corresponding to numeric features in the DataFrame.

    Returns:
    - X (pandas.DataFrame): The features extracted from the input DataFrame.
    - y (pandas.Series): The target variable extracted from the "survival_status" column of the input DataFrame.

    Usage:
    >>> X, y = split_x_y(df, word_features, categorical_features, numeric_features)
    """

    X = df[word_features + categorical_features + numeric_features]
    y = df["survival_status"]
    return X, y

@click.command()
@click.option('--business-data', type=str, required=True, help="Path to training and test data") #"data/processed/business_econ.csv"
@click.option('--test-data-to', type=str, required=True, help="Path to save the test data") #"data/processed/"
@click.option('--pipeline-to', type=str, required=True, help="Path to directory where the pipeline object will be written to") #"results/models/"
@click.option('--seed', type=int, help="Random seed", default=123)
def main(business_data, test_data_to, pipeline_to, seed):

    #business econ
    #seed or random state
    #--pipeline-to model save
    #-save transformer, might need it later
    # save score?
    business_econ = pd.read_csv(business_data)
    train_df, test_df = train_test_split(business_econ, test_size=0.3, random_state=seed)

    test_df.to_csv(test_data_to + "license_test.csv", index=False)

    features = {
        'word_features': ['BusinessType'],
        'categorical_features': ['City', 'LocalArea'],
        'numeric_features': ['NumberofEmployees', 'FeePaid', 
                            'GDPValue', 'ConsumerPriceValue', 'EmploymentValue', 'InvestmentConstructionValue']
    }
    
    X_train, y_train = split_x_y(train_df, **features)
    X_test, y_test = split_x_y(test_df, **features)
    
    X_train_transformed = transform(X_train, **features)
    X_test_transformed = transform(X_test, **features)

    bnb = BernoulliNB()
    pd.DataFrame(cross_validate(bnb, X_train_transformed, y_train, cv=10, return_train_score=True))

    logreg = LogisticRegression(random_state=seed, max_iter=1000)
    pd.DataFrame(cross_validate(logreg, X_train_transformed, y_train, cv=10, return_train_score=True))

    logreg.fit(X_test_transformed, y_test)

    model_path = pipeline_to + "lr_license_renewal_pipeline.pickle"
    with open(os.path.join(model_path), 'wb') as f:
        pickle.dump(logreg, f)
    
    print(logreg.score(X_test_transformed, y_test))

if __name__ == "__main__":
    main()