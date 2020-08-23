# - *- coding utf- 8 - *-

import datetime

import pandas_datareader.data as web
import yfinance as yf


def get_stock_info(stock_id):
    tw_stock_id = f'{stock_id}.TW'
    rs = yf.Ticker(tw_stock_id)
    return rs.info
    
def get_stock_dataset(stock_id):
    tw_stock_id = f'{stock_id}.TW'
    yf.pdr_override()
    start = datetime.datetime(2019, 1, 1)
    end = datetime.datetime(2020, 7, 1)
    df = web.get_data_yahoo(['2884.TW'],start, end)
    return df

df = get_stock_dataset('2884')
df.reset_index(inplace=True)
print(df)
