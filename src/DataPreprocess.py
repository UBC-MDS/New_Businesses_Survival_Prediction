import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

import numpy as np
import datetime as dt
from functools import reduce
"""
Preprocess business_license as dataframe,
and turn a dictionary storing the economic dataframes into one merged and clean dataframe.

Example
-------
>>> from DataPreprocess import *
>>> business = business_datacleaning(business = business, survival_threshold = 365 * 2)
>>> econ = econ_datacleaning(raw_econ_index_data_dict)
>>> business_econ = merge_business_econ_by_year(business, econ)
"""

def business_datacleaning(business, survival_threshold=730):
    """
    Performs data cleaning on a business DataFrame.

    Parameters:
    - business (pandas.DataFrame): The input DataFrame containing business-license data.
    - survival_threshold (int, optional): The threshold for defining the survival status of a business in days. Defaults to 730 days.

    Returns:
    - pandas.DataFrame: The cleaned and processed DataFrame with added features.
    """
    # Drop rows where ExpiredDate and IssuedDate are NA
    business = business.dropna(subset = ["ExpiredDate", "IssuedDate"])

    # Transform ExpiredDate and IssuedDate to date
    business[["ExpiredDate", "IssuedDate"]] = business[["ExpiredDate", "IssuedDate"]].apply(pd.to_datetime, utc=True)
    business['ExpiredDate'] = business['ExpiredDate'].dt.date
    business['IssuedDate'] = business['IssuedDate'].dt.date

    # Calculate the survival interval of each company
    business['survival_days'] = (business.groupby('BusinessName')['ExpiredDate'].transform('max')-
                                business.groupby('BusinessName')['IssuedDate'].transform('min'))
    business['survival_days'] = pd.to_timedelta(business['survival_days']).dt.days

    # Keep only the first issued record of each company (to obtain the year when a company starts it business)
    business.sort_values(by='ExpiredDate', ascending=True)
    business = business.drop_duplicates(subset='BusinessName', keep='first')

    # Filter to keep those records where the first `ExpiredDate` is before or equal to year 2022.
    business = business[business['ExpiredDate'] <= dt.date(2022, 12, 31)]

    # Adjust format of FOLDERYEAR
    business['FOLDERYEAR'] = business['FOLDERYEAR'].apply(lambda x : '20' + str(x))
    
    # Create target column and adjust Boolean to 0, 1
    business['survival_status'] = business['survival_days'] >= survival_threshold
    business["survival_status"] = business["survival_status"].astype(int)
    return business


def econ_datacleaning(raw_econ_index_data_dict):
    """
    Cleans and processes economic data from a dictionary of DataFrames.

    Parameters:
    - raw_econ_index_data_dict (dict): A dictionary containing raw economic data, where keys are indicator names and values are DataFrames.

    Returns:
    - pandas.DataFrame: The cleaned and processed DataFrame containing economic data.
    """
    econList = []
    for index_name, data in raw_econ_index_data_dict.items():
        data = data[['REF_DATE', 'VALUE']]
        data['REF_YEAR'] = data['REF_DATE'].apply(lambda x : int(str(x)[:4]))
        data = data[data['REF_YEAR'] >= 2012]
        data['REF_YEAR'] = data['REF_YEAR'].astype(str)
        data = data.drop(columns=['REF_DATE'])
        econList.append(data.rename(columns = {'VALUE': f'{index_name}Value', 
                                                'REF_YEAR': 'FOLDERYEAR'}
                                    ).groupby('FOLDERYEAR').mean().reset_index())
        
    return reduce(lambda df1, df2 : pd.merge(df1, df2, on=['FOLDERYEAR'], how='inner'), econList).drop_duplicates()
    

def merge_business_econ_by_year(business, econ):
    """
    Merges business-license data and economic data based on the 'FOLDERYEAR' column..

    Parameters:
     - business (pandas.DataFrame): The DataFrame containing business-license data.
     - econ (pandas.DataFrame): The DataFrame containing economic data.

    Returns:
    - pandas.DataFrame: The merged DataFrame containing both business and economic data.
    """
    return business.merge(econ, on='FOLDERYEAR', how='left')
