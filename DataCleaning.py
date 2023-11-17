import pandas as pd
import numpy as np
import datetime as dt

def datacleaning(business, survival_threshold):
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

    business['survival_status'] = business['survival_days'] >= survival_threshold
    # Adjust Boolean to 0, 1
    business["survival_status"] = business["survival_status"].astype(int)
    return business