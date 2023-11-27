import pandas as pd
import datetime as dt
import os
import argparse

# * setup argument parser
parser = argparse.ArgumentParser(prog='TV Processor', description='Process data into an appropriate format to feed to TradingView', epilog='Enjoy it!')

FILENAME = 'aaii_bullish_pct_raw'
path = os.path.join('content', FILENAME + '.csv')
df = pd.read_csv(path, parse_dates=['date'])

df = df.sort_values(by='date')
df['date'] = df['date'].apply(lambda d: dt.datetime.strftime(d, '%Y%m%d') + 'T')
df['volume'].fillna(0.0, inplace=True)
df = df.drop_duplicates(subset=['date'], keep='last')
# print(df.head())

# forward fill values
for c in df.columns:
    df[c] = df[c].fillna(method='ffill')

# TODO: validate data
assert df.isnull().sum().sum() == 0, 'Data contains missing values'

export_name = FILENAME.replace('_raw', '').upper()
export_path = os.path.join('data', export_name + '.csv')
df.to_csv(export_path, index=False, header=False)