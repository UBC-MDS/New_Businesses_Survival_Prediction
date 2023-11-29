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

# test input data type of visualization function: data
def test_visualization_input_type():
    assert isinstance(business_econ_df, pd.DataFrame), "`numeric_feature_visualization` should be input with a pandas data frame"

# test necessary features for visualization are included in the whole dataset
def test_visualization_input_value():
    visualized_features = ['GDPValue', 'ConsumerPriceValue', 'EmploymentValue', 'InvestmentConstructionValue', 'NumberofEmployees', 'FeePaid', 'LocalArea', 'BusinessType'] #target features for visualization
    assert set(visualized_features).issubset(set(business_econ_df.columns)), f"`numeric_feature_visualization` did not get necessary columns. Columns should contain: {visualized_features}"
