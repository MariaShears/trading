import pandas as pd
from pandas import json_normalize


def clean_earnings(raw_earnings): 
    earnings_df = json_normalize(raw_earnings['quarterlyEarnings'])
    earnings_df = earnings_df[['reportedDate', 'surprise', 'surprisePercentage']]
    earnings_df['surprise'] = pd.to_numeric(earnings_df['surprise'], errors='coerce')
    earnings_df['surprisePercentage'] = pd.to_numeric(earnings_df['surprisePercentage'], errors='coerce')
    earnings_df['reportedDate'] = pd.to_datetime(earnings_df['reportedDate'])
    earnings_df.dropna(inplace=True)
    return earnings_df