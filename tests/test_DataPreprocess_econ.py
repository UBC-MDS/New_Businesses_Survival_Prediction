import pandas as pd
from pandas.core.dtypes.common import is_timedelta64_dtype
from pandas.api.types import is_integer_dtype

import pytest
import sys
import os

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.DataFetch import *
from src.DataPreprocess import *

# Load data
business_df = fetch_business_license()
econ_dict = fetch_econ_indicators()

business_df = business_datacleaning(business = business_df, survival_threshold = 365 * 2)
econ_df = econ_datacleaning(econ_dict)
business_econ_df = merge_business_econ_by_year(business_df, econ_df)

# econ data frame - Test for correct return type
def test_econ_datacleaning_return_dataframe():
    assert isinstance(econ_df, pd.DataFrame), "`fetch_business_license` should return a pandas data frame"

# econ data frame - Test for the necessary columns are included in the loaded data frame
def test_econ_contains_necessary_columns():
    econ_necessary_col = ['GDPValue', 'ConsumerPriceValue', 'EmploymentValue', 'InvestmentConstructionValue']
    assert set(econ_necessary_col).issubset(set(econ_df.columns)), f"`econ_datacleaning` did not get necessary columns. Columns should contain: {econ_necessary_col}"

def test_merge_return_dataframe():
    assert isinstance(business_econ_df, pd.DataFrame), "`merge_business_econ_by_year` should return a pandas data frame"