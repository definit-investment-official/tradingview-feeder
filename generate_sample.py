import pandas as pd
import numpy as np
import datetime as dt

START_DATE = dt.date(2001, 1, 1)
END_DATE = dt.date(2023, 11, 30)
MIN_VALUE = 10
MAX_VALUE = 20
MIN_VOLUME = 1000
MAX_VOLUME = 5000

# dates = [d.date() for d in pd.date_range(START_DATE, END_DATE)]
# date_str = [dt.datetime.strftime(d, '%Y%m%d') + 'T' for d in dates]

def generate_random_OHLCV(start_date, end_date, min_value, max_value, min_volume, max_volume):
    # Generate random datetime index between start_date and end_date
    date_range = pd.date_range(start=start_date, end=end_date)
    date_str = [dt.datetime.strftime(d, '%Y%m%d') + 'T' for d in date_range]
    num_rows = len(date_range)
    
    # Generate random OHLCV data
    open_prices = np.random.uniform(min_value, max_value, num_rows)
    high_prices = [max(open_price, np.random.uniform(open_price, 1.5 * open_price)) for open_price in open_prices]
    low_prices = [min(open_price, np.random.uniform(0.5 * open_price, open_price)) for open_price in open_prices]
    close_prices = np.random.uniform(low_prices, high_prices)
    volumes = np.random.randint(min_volume, max_volume, num_rows)
    
    # Create DataFrame
    data = {'Date': date_str,
            'Open': open_prices,
            'High': high_prices,
            'Low': low_prices,
            'Close': close_prices,
            'Volume': volumes}
    
    df = pd.DataFrame(data)
    return df

random_df = generate_random_OHLCV(START_DATE, END_DATE, MIN_VALUE, MAX_VALUE, MIN_VOLUME, MAX_VOLUME)
random_df.to_csv('data/TEST_RANDOM.csv', index=False, header=False)