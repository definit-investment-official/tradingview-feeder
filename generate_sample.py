import pandas as pd
import numpy as np
import datetime as dt

START_DATE = dt.date(2001, 1, 1)
END_DATE = dt.date(2023, 11, 30)
MIN_VALUE = 10
MAX_VALUE = 20

dates = [d.date() for d in pd.date_range(START_DATE, END_DATE)]
date_str = [dt.datetime.strftime(d, '%Y%m%d') + 'T' for d in dates]

random_samples = np.random.uniform(MIN_VALUE, MAX_VALUE, size=(len(dates), 5))
random_df = pd.DataFrame(random_samples)
random_df.insert(0, 'date', date_str)
random_df.to_csv('data/TEST_RANDOM.csv', index=False, header=False)