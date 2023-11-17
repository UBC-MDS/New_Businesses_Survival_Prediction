import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'

import numpy as np
import datetime as dt
from functools import reduce

def business_datacleaning(business, survival_threshold):
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

    # Filter to keep those records where the latest `ExpiredDate` is before or equal to year 2022.
    business = business[business['ExpiredDate'] <= dt.date(2022, 12, 31)]

    # Adjust format of FOLDERYEAR
    business['FOLDERYEAR'] = business['FOLDERYEAR'].apply(lambda x : '20' + str(x))
    
    # Create target column and adjust Boolean to 0, 1
    business['survival_status'] = business['survival_days'] >= survival_threshold
    business["survival_status"] = business["survival_status"].astype(int)
    return business


def econ_datacleaning(raw_econ_index_data_dict):
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
    return business.merge(econ, on='FOLDERYEAR', how='left')
