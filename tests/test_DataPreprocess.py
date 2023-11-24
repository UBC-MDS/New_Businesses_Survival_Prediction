import pandas as pd
from pandas.core.dtypes.common import is_timedelta64_dtype
from pandas.api.types import is_datetime64_any_dtype

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

# Test for correct return type
def test_business_datacleaning_data_type():
    assert is_datetime64_any_dtype(business_df['IssuedDate']), "Column `IssuedDate` in business_df from `fetch_business_license` should be datetime"
    assert is_datetime64_any_dtype(business_df['ExpiredDate']), "Column `IssuedDate` in business_df from `fetch_business_license` should be datetime"

def test_business_datacleaning_target_value():
    assert set([1, 0]).issubset(business_df['survival_status'].unique()), "Column `IssuedDate` in business_df from `fetch_business_license` should contain only [1, 0]"


def test_econ_datacleaning():
    assert isinstance(econ_dict, dict), "`fetch_econ_indicators` should return a dictionary"
    assert len(econ_dict) == 4, "`fetch_econ_indicators` should return a dictionary with 4 items"
    for df in econ_dict.values():
        assert isinstance(df, pd.DataFrame), "One of the item is not a pandas data frame"

# Test for the necessary columns are included in the loaded data frames
def test_business_contains_necessary_columns():
    busi_necessary_col = ['BusinessType', 'City', 'LocalArea', 'NumberofEmployees', 'FeePaid']
    assert set(busi_necessary_col).issubset(set(business_df.columns)), f"`fetch_business_license` did not get necessary columns. Columns should contain: {busi_necessary_col}"