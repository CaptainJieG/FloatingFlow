# 导入tushare
import pandas as pd
import tushare as ts

token_dataframe = pd.read_fwf('tushare.token', nrows=1, header=None, index_col=None)

# 初始化pro接口
pro = ts.pro_api(token_dataframe.loc[0].iat[0])

# 拉取数据
dataframe = pro.daily(**{
    "ts_code": "000815.sz",
    "trade_date": "",
    "start_date": 20220101,
    "end_date": 20220219,
    "offset": "",
    "limit": ""
}, fields=[
    "ts_code",
    "trade_date",
    "open",
    "high",
    "low",
    "close",
    "pre_close",
    "change",
    "pct_chg",
    "vol",
    "amount"
])
print(dataframe)

dataframe.to_csv("test.csv", index=False, sep=',')
