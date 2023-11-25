import pandas as pd
import numpy as np
import datetime
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.Modeling import *

# test data
test_data_dict = {
    "FOLDERYEAR": {
        24601: "2013",
        17675: "2013",
        65629: "2015",
        74385: "2021",
        61577: "2019",
    },
    "LicenceRSN": {
        24601: 1788833,
        17675: 1776276,
        65629: 2625134,
        74385: 3722389,
        61577: 3239504,
    },
    "LicenceNumber": {
        24601: "13-169417",
        17675: "13-156865",
        65629: "15-319323",
        74385: "21-139873",
        61577: "19-113980",
    },
    "LicenceRevisionNumber": {24601: 0, 17675: 0, 65629: 0, 74385: 0, 61577: 0},
    "BusinessName": {
        24601: "(Giuseppe Mezzarobba)",
        17675: "Halco Software Systems Ltd",
        65629: "(Jeremy Hodgins)",
        74385: "Canadian Disinfection Corp",
        61577: "Dogbo Delivery Services Inc",
    },
    "BusinessTradeName": {
        24601: np.nan,
        17675: np.nan,
        65629: "Grizzly Tuff Coatings",
        74385: np.nan,
        61577: np.nan,
    },
    "Status": {
        24601: "Issued",
        17675: "Issued",
        65629: "Issued",
        74385: "Issued",
        61577: "Issued",
    },
    "IssuedDate": {
        24601: datetime.date(2012, 11, 30),
        17675: datetime.date(2013, 1, 3),
        65629: datetime.date(2015, 11, 20),
        74385: datetime.date(2020, 12, 29),
        61577: datetime.date(2019, 4, 2),
    },
    "ExpiredDate": {
        24601: datetime.date(2013, 12, 31),
        17675: datetime.date(2013, 12, 31),
        65629: datetime.date(2015, 12, 31),
        74385: datetime.date(2021, 12, 31),
        61577: datetime.date(2019, 12, 31),
    },
    "BusinessType": {
        24601: "One-Family Dwelling",
        17675: "Computer Services",
        65629: "Contractor - Special Trades",
        74385: "Office",
        61577: "Moving/Transfer Service",
    },
    "BusinessSubType": {
        24601: np.nan,
        17675: "Software",
        65629: "Other",
        74385: "Administration",
        61577: "Goods",
    },
    "Unit": {24601: np.nan, 17675: "505", 65629: np.nan, 74385: np.nan, 61577: np.nan},
    "UnitType": {24601: np.nan, 17675: "Unit", 65629: np.nan, 74385: np.nan, 61577: np.nan},
    "House": {24601: np.nan, 17675: "601", 65629: np.nan, 74385: np.nan, 61577: np.nan},
    "Street": {24601: np.nan, 17675: "W Broadway", 65629: np.nan, 74385: np.nan, 61577: np.nan},
    "City": {
        24601: "Vancouver",
        17675: "Vancouver",
        65629: "Vancouver",
        74385: "Vancouver",
        61577: "Vancouver",
    },
    "Province": {24601: "BC", 17675: "BC", 65629: "BC", 74385: "BC", 61577: "BC"},
    "Country": {24601: "CA", 17675: "CA", 65629: "CA", 74385: "CA", 61577: "CA"},
    "PostalCode": {24601: np.nan, 17675: "V5Z 4C2", 65629: np.nan, 74385: np.nan, 61577: np.nan},
    "LocalArea": {
        24601: "Marpole",
        17675: "Fairview",
        65629: "Downtown",
        74385: "Arbutus-Ridge",
        61577: "Sunset",
    },
    "NumberofEmployees": {24601: 0.0, 17675: 0.0, 65629: 0.0, 74385: 1.0, 61577: 1.0},
    "FeePaid": {24601: 62.0, 17675: 129.0, 65629: 79.0, 74385: 207.0, 61577: 191.0},
    "ExtractDate": {
        24601: "2019-07-21T13:49:06-07:00",
        17675: "2019-07-21T13:49:06-07:00",
        65629: "2019-07-21T13:49:21-07:00",
        74385: "2023-11-01T02:38:56-07:00",
        61577: "2022-01-01T02:32:01-08:00",
    },
    "Geom": {
        24601: np.nan,
        17675: '{"coordinates": [-123.118596122757, 49.2635657969344], "type": "Point"}',
        65629: np.nan,
        74385: np.nan,
        61577: np.nan,
    },
    "geo_point_2d": {
        24601: np.nan,
        17675: "49.2635657969344, -123.118596122757",
        65629: np.nan,
        74385: np.nan,
        61577: np.nan,
    },
    "survival_days": {
        24601: 1126.0,
        17675: 4014.0,
        65629: 41.0,
        74385: 1097.0,
        61577: 545.0,
    },
    "survival_status": {24601: 1, 17675: 1, 65629: 0, 74385: 1, 61577: 0},
    "GDPValue": {
        24601: 1754172.8333333333,
        17675: 1754172.8333333333,
        65629: 1820025.9166666667,
        74385: 1991978.0833333333,
        61577: 1996743.9166666667,
    },
    "ConsumerPriceValue": {
        24601: 1.2750000000000001,
        17675: 1.2750000000000001,
        65629: 1.9000000000000001,
        74385: 2.5500000000000003,
        61577: 2.1666666666666665,
    },
    "EmploymentValue": {
        24601: 2320.475,
        17675: 2320.475,
        65629: 2390.0,
        74385: 2665.4166666666665,
        61577: 2676.116666666667,
    },
    "InvestmentConstructionValue": {
        24601: 987533855.0,
        17675: 987533855.0,
        65629: 1146144428.9166667,
        74385: 1504690265.5,
        61577: 1657492504.75,
    },
}
df = pd.DataFrame(test_data_dict)

features = {
    'word_features': ['BusinessType'],
    'categorical_features': ['City', 'LocalArea'],
    'numeric_features': ['NumberofEmployees', 'FeePaid', 
                        'GDPValue', 'ConsumerPriceValue', 'EmploymentValue', 'InvestmentConstructionValue']
}

X_df, y_df = split_x_y(df, **features)
X_transformed = transform(X_df, **features)


# split_x_y - Test for correct return type
def test_split_x_y_return_dataframe():
    assert isinstance(X_df, pd.DataFrame), "`split_x_y` return X is not a pandas dataframe. Should return a pandas dataframe"
    assert isinstance(y_df, pd.Series), "`split_x_y` return y is not a pandas dataframe. Should return a pandas dataframe"

# split_x_y - Test for correct return columns
def test_split_x_y_return_columns():
    assert X_df.columns.tolist() == [c for cols in features.values() for c in cols], f"`split_x_y` return X should have columns: {[c for cols in features.values() for c in cols]}. Return {X_df.columns} instead."
    assert len(X_df.columns.tolist()) == 9, "Getting more than expected columns in training dataframe"

# transform - Test for correct return type
def test_transform_return_dataframe():
    assert isinstance(X_transformed, np.ndarray), "`transform` should return an array"

# transform - Test for correct return column types
def test_transform_return_numeric_columns():
    existed_cols_cnt = X_transformed.shape[1]
    numeric_cols_cnt = pd.DataFrame(X_transformed).select_dtypes(include=np.number).shape[1]
    assert existed_cols_cnt == numeric_cols_cnt, "`transform` should return all numeric columns. There are some non-numeric columns instead."