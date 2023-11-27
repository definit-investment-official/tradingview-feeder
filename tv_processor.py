import pandas as pd
import datetime as dt
import argparse

# * setup argument parser
parser = argparse.ArgumentParser(prog='TV Processor', description='Process data into an appropriate format to feed to TradingView', epilog='Enjoy it!')
parser.add_argument('--data_path', help='Path of raw data')
parser.add_argument('--export_path', help='Path of processed data', default=None)
args = parser.parse_args()
data_path = args.data_path
export_path = args.export_path

# ? if export_path is not defined, use the uppercase version of data_path
if not export_path:
    export_path = data_path.replace('.csv', '').upper() + '.csv'

# FILENAME = 'aaii_bullish_pct_raw'
# path = os.path.join('content', FILENAME + '.csv')
df = pd.read_csv(data_path, parse_dates=['date'])

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

df.to_csv(export_path, index=False, header=False)