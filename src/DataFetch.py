import zipfile
from urllib.request import urlopen
import shutil
import os
import pandas as pd
from collections import defaultdict
from functools import reduce
import click

"""
Fetch data via URLs.

Usage
-------
>>> from DataFetch import fetch_business_license, fetch_econ_indices
>>> business = fetch_business_license()
>>> raw_econ_index_data_dict = fetch_econ_indicators()

>>> raw_econ_index_data_dict
raw_econ_index_data_dict = {
    'GDP': gdp_df,
    'ConsumerPrice': cp_df,
    'Employment': employment_df,
    'InvestmentConstruction': investment_df
}

"""

def fetch_business_license():
    print('Now loading: business_license data')
    url = 'https://opendata.vancouver.ca/api/explore/v2.1/catalog/datasets/business-licences/exports/csv?lang=en&timezone=America%2FLos_Angeles&use_labels=true&delimiter=%3B'
    return pd.read_csv(url, delimiter = ';', low_memory=False)


def extrat_from_zip(url):
    """
    Extracts and loads data from a CSV file contained within a zip archive from a given URL.

    Parameters:
    - url (str): The URL of the zip archive containing the CSV file.

    Returns:
    - pandas.DataFrame: The extracted CSV data loaded into a pandas DataFrame.

    Usage:
    >>> extracted_data = extrat_from_zip('https://example.com/data.zip')
    """
    # extracting zipfile from URL
    zip_name = 'temp.zip'
    with urlopen(url) as response, open(zip_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

        # extracting required file from zipfile
        with zipfile.ZipFile(zip_name) as zf:
            for csv_name in zf.namelist():
                if 'MetaData' not in csv_name:
                    zf.extract(csv_name)
                    data = pd.read_csv(csv_name, low_memory=False)
                    break

    os.remove(zip_name)
    os.remove(csv_name)

    return data

def customized_filter(index_name, data):
    """
    Filters and extracts specific economic index data from a given DataFrame based on the provided index name.

    Parameters:
    - index_name (str): The economic indicators to filter. Must be one of ['GDP', 'ConsumerPrice', 'Employment', 'InvestmentConstruction'].
    - data (pandas.DataFrame): The input DataFrame containing economic data.

    Returns:
    - pandas.DataFrame: A filtered DataFrame containing data specific to the provided economic indicator names.

    Raises:
    - AssertionError: If the provided index_name is not one of ['GDP', 'ConsumerPrice', 'Employment', 'InvestmentConstruction'].
    """

    assert index_name in ['GDP', 'ConsumerPrice', 'Employment', 'InvestmentConstruction'],  "Economic index not in ['GDP', 'ConsumerPrice', 'Employment', 'InvestmentConstruction']"

    if index_name == 'GDP':
        mask = (data['North American Industry Classification System (NAICS)'] == 'All industries [T001]') & \
                (data['Prices'] == '2012 constant prices') & \
                (data['Seasonal adjustment'] == 'Seasonally adjusted at annual rates')

    elif index_name == 'ConsumerPrice':
        mask = (data['UOM'] == 'Percent') & \
                (data['Alternative measures'] == 'Measure of core inflation based on a factor model, CPI-common (year-over-year percent change)')

    elif index_name == 'Employment':
        mask = (data['GEO'] == 'British Columbia') & \
                (data['North American Industry Classification System (NAICS)'] == 'Total employed, all industries') & \
                (data['Statistics'] == 'Estimate')  & \
                (data['Data type'] == 'Seasonally adjusted')

    elif index_name == 'InvestmentConstruction':
        mask = (data['GEO'] == 'Vancouver, British Columbia') & \
                (data['Type of structure'] == 'Total residential and non-residential') & \
                (data['Type of work'] == 'Types of work, total')  & \
                (data['Investment Value'] == 'Seasonally adjusted - current')
        
    return data[mask].dropna(subset=['REF_DATE', 'VALUE'])

def fetch_econ_indicators():
    """
    Fetches and preprocesses economic indicators data from specified URLs.

    Returns:
    - dict: A dictionary containing economic indicators dataframes, where keys are indicator names.

    Usage:
    >>> econ_data = fetch_econ_indicators()
    """
    econ_url_dict = {
        'GDP': 'https://www150.statcan.gc.ca/n1/en/tbl/csv/36100434-eng.zip?st=8pJW1bGZ',
        'ConsumerPrice': 'https://www150.statcan.gc.ca/n1/en/tbl/csv/18100256-eng.zip?st=-S3x83UK',
        'Employment': 'https://www150.statcan.gc.ca/n1/en/tbl/csv/14100355-eng.zip?st=As1I3Vuk',
        'InvestmentConstruction': 'https://www150.statcan.gc.ca/n1/en/tbl/csv/34100175-eng.zip?st=MNl94riS'
    }

    econ_data_dict = defaultdict()

    for index_name, url in econ_url_dict.items():
        print(f'Now loading: {index_name} data')
        econ_data_dict[index_name] = customized_filter(index_name, extrat_from_zip(url))

    return econ_data_dict

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
        data.loc[:, 'REF_YEAR'] = data.loc[:, 'REF_DATE'].apply(lambda x : int(str(x)[:4]))
        data = data[data['REF_YEAR'] >= 2012]
        data['REF_YEAR'] = data['REF_YEAR'].astype(str)
        data = data.drop(columns=['REF_DATE'])
        econList.append(data.rename(columns = {'VALUE': f'{index_name}Value', 
                                                'REF_YEAR': 'FOLDERYEAR'}
                                    ).groupby('FOLDERYEAR').mean().reset_index())
        
    return reduce(lambda df1, df2 : pd.merge(df1, df2, on=['FOLDERYEAR'], how='inner'), econList).drop_duplicates()
    
@click.command()
@click.option('--raw_business_path') # raw_business_path=data/raw/business.csv
@click.option('--raw_econ_path') # raw_econ_path=data/raw/econ.csv
def main(raw_business_path, raw_econ_path):
    business = fetch_business_license()
    raw_econ_index_data_dict = fetch_econ_indicators()
    econ = econ_datacleaning(raw_econ_index_data_dict)

    business.to_csv(raw_business_path, index=False)
    econ.to_csv(raw_econ_path, index=False)

if __name__ == "__main__":
    main()

# python src/DataFetch.py --raw_business_path=data/raw/business.csv --raw_econ_path=data/raw/econ.csv