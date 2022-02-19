import mplfinance as mpf
import pandas as pd

dataframe = pd.read_csv('test.csv',
                        skiprows=0,
                        parse_dates=['trade_date'],
                        index_col=['trade_date'])

my_color = mpf.make_marketcolors(up='red',
                                 down='green',
                                 edge='inherit')

my_style = mpf.make_mpf_style(marketcolors=my_color)

mpf.plot(dataframe, type='candle',
         ylabel="price(usdt)",
         style=my_style)
