import pandas as pd
import pytest
import sys
import os

# Import the count_classes function from the src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.DataFetch import *

# Load data
business_df = fetch_business_license()
econ_dict = fetch_econ_indicators()

# Test for correct return type
def test_business_returns_dataframe():
    assert isinstance(business_df, pd.DataFrame), "`fetch_business_license` should return a pandas data frame"

def test_econ_returns_dict():
    assert isinstance(econ_dict, dict), "`fetch_econ_indicators` should return a dictionary"
    assert len(econ_dict) == 4, "`fetch_econ_indicators` should return a dictionary with 4 items"
    for df in econ_dict.values():
        assert isinstance(df, pd.DataFrame), "One of the item is not a pandas data frame"

# Test for the necessary columns are included in the loaded data frames
def test_():
    busi_necessary_col = ['BusinessType', 'City', 'LocalArea', 'NumberofEmployees', 'FeePaid']
    assert set(busi_necessary_col).issubset(set(business_df.columns)), f"`fetch_business_license` did not get necessary columns. Columns should contain: {busi_necessary_col}"