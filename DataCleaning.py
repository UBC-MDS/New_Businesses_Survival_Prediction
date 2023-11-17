import pandas as pd
import numpy as np
import datetime as dt

def business_datacleaning(self, business, survival_threshold):
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

    # Keep only the newest issued record of each company
    business.sort_values(by='ExpiredDate', ascending=True)
    business = business.drop_duplicates(subset='BusinessName', keep='last')

    # Filter to keep those records where the latest `ExpiredDate` is before or equal to year 2022.
    business = business[business['ExpiredDate'] <= dt.date(2022, 12, 31)]

    # Adjust format of FOLDERYEAR
    business['FOLDERYEAR'] = business['FOLDERYEAR'].apply(lambda x : '20' + str(x))
    
    # Create target colum and adjust Boolean to 0, 1
    business['survival_status'] = business['survival_days'] >= survival_threshold
    business["survival_status"] = business["survival_status"].astype(int)
    return business

def gdp_datacleaning(gdp):
    gdp = gdp[gdp['North American Industry Classification System (NAICS)'] == 'All industries [T001]'][['REF_DATE', 'VALUE']]
    gdp['REF_YEAR'] = gdp['REF_DATE'].apply(lambda x : str(x)[:4])
    gdp = gdp[gdp['REF_YEAR'] >= 2012]
    gdp['REF_DATE'] = pd.to_datetime(gdp['REF_DATE'])
    gdp['REF_YEAR'] = gdp['REF_YEAR'].astype(str)
    return gdp.rename(columns = {'VALUE': 'GdpValue', 'REF_YEAR': 'FOLDERYEAR'})

def merge_business_econ_by_year(business, econ):
    return business.merge(econ, on='FOLDERYEAR', how='inner')