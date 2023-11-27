import pandas as pd
import datetime as dt
import os

FILENAME = 'aaii_bullish_pct_raw'
path = os.path.join('content', FILENAME + '.csv')
raw_df = pd.read_csv(path, parse_dates=['date'])

raw_df = raw_df.sort_values(by='date')
raw_df['date'] = raw_df['date'].apply(lambda d: dt.datetime.strftime(d, '%Y%m%d') + 'T')
raw_df['volume'].fillna(0.0, inplace=True)
raw_df = raw_df.drop_duplicates(subset=['date'], keep='last')
# print(raw_df.head())

# forward fill values
for c in raw_df.columns:
    raw_df[c] = raw_df[c].fillna(method='ffill')

# TODO: validate data
assert raw_df.isnull().sum().sum() == 0, 'Data contains missing values'

export_name = FILENAME.replace('_raw', '').upper()
export_path = os.path.join('data', export_name + '.csv')
raw_df.to_csv(export_path, index=False, header=False)