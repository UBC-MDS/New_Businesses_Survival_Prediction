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

# business data frame - Test for correct target value
def test_business_datacleaning_target_value():
    assert is_integer_dtype(business_df['survival_status']), "Column `survival_status` in business_df from `fetch_business_license` should be an integer"
    assert set([1, 0]) == set(business_df['survival_status'].unique()), "Column `IssuedDate` in business_df from `fetch_business_license` should contain only either 1 or 0"