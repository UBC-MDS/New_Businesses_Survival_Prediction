import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

import numpy as np
import datetime as dt
import click

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


@click.command()
@click.option('--raw_business_path') # raw_business_path = 'data/raw/business.csv'
@click.option('--processed_business_path') # processed_business_path = 'data/processed/business.csv'
@click.option('--raw_econ_path') # business_path = 'data/raw/econ.csv'
@click.option('--merged_data_output_path') # merged_data_output_path = 'data/processed/business_econ.csv'
def main(raw_business_path, processed_business_path, raw_econ_path, merged_data_output_path):
    business = pd.read_csv(raw_business_path, low_memory=False)
    business = business_datacleaning(business = business, survival_threshold = 365 * 2)
    business.to_csv(processed_business_path, index=False)
    
    econ = pd.read_csv(raw_econ_path, low_memory=False)
    business['FOLDERYEAR'] = business['FOLDERYEAR'].astype(str)
    econ['FOLDERYEAR'] = econ['FOLDERYEAR'].astype(str)

    business_econ = merge_business_econ_by_year(business, econ)
    business_econ.to_csv(merged_data_output_path, index=False)

if __name__ == "__main__":
    main()

# python src/DataPreprocess.py --raw_business_path=data/raw/business.csv --processed_business_path=data/processed/business.csv --raw_econ_path=data/raw/econ.csv --merged_data_output_path=data/processed/business_econ.csv