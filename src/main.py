from datetime import datetime, timedelta
from telnetlib import PRAGMA_HEARTBEAT
from matplotlib.pyplot import title
import yfinance as yf
from pytickersymbols import PyTickerSymbols
import pandas as pd
import matplotlib.pyplot as plt


ticker = "AAPL"
stock = yf.Ticker(ticker)
#print(stock.info)

stocks = PyTickerSymbols();
tickers = stocks.get_all_countries()
#print(tickers)
all_ticker_getter_names = list(filter(
    lambda x: (
        x.endswith('_google_ticker') or x.endswith('_yahoo_tickers')
    ),
    dir(stocks),
))
#print(len(all_ticker_getter_names))

# sp500 = stocks.get_sp_500_nyc_yahoo_tickers()
# print(len(sp500))
DATE_FORMAT = "%Y-%m-%d"
days = 3*365;
now = datetime.now()
startDate = now - timedelta(days=days)

today = now.strftime(DATE_FORMAT)
startStr = "1980-12-12" #startDate.strftime(DATE_FORMAT)
df = yf.download(ticker, start=startStr, end=today)
df.reset_index(inplace=True)
df['Ticker'] = ticker
print(df.head())
print('데이터사이즈: ', df.shape)
print('행의 레이블: ', df.index)
print('열의 레이블: ', df.columns)
print('결측치: ', df.isnull().sum())
# 문제의 기준
# 위험성 
# 변동성 -> 변화율 
# (New - Old) / Old  => (close - open) / open * 100

# print(df.head())
#df1 = df.copy()
needColumn = ['Date', 'Open', 'Close', 'Ticker']
df1 = pd.DataFrame(df[needColumn])
print(df1.head())
# 변화율계산
df1['change_1_percent'] = (df1['Close'] - df1['Open']) / df1['Open'] * 100
# 결측치
print(df1['change_1_percent'].isnull().sum())
# 통계요약 
print(df1['change_1_percent'].describe())
print(df1['change_1_percent'].tail().describe())
#print(df1.head())
# 분포확인 
ax = df1['change_1_percent'].plot.hist(bins=50, title=ticker)
#print(ax)

#plt.hist(df1['change_1_percent'], bins=50, title=ticker)
#plt.show()

# 변동폭이 3이상인

#print( len(df1[ df1['change_1_percent'] > 3]) )
#print(df1[ df1['change_1_percent'] > 3])

#  하루 주가변화율 표준화 
df1['change_1_percent_s'] = (df1['change_1_percent'] - df1['change_1_percent'].mean()) / df1['change_1_percent'].std()
print(df1.tail())