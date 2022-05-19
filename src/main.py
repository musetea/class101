from traceback import print_tb
from tracemalloc import stop
import yfinance as yf
from pytickersymbols import PyTickerSymbols


ticker = "AXP"
stock = yf.Ticker(ticker)
print(stock.info)

stocks = PyTickerSymbols();
tickers = stocks.get_all_countries()
print(tickers)
all_ticker_getter_names = list(filter(
    lambda x: (
        x.endswith('_google_ticker') or x.endswith('_yahoo_tickers')
    ),
    dir(stocks),
))
print(len(all_ticker_getter_names))

sp500 = stocks.get_sp_500_nyc_yahoo_tickers()
print(len(sp500))