from pytickersymbols import PyTickerSymbols
import yfinance as yf
from db import mongo

DB_NAME:str = "sp500"
COLLECTION_NAME:str = "tickers"


tickers = [];




def getTicker():
    symbols = PyTickerSymbols()
    tickers = symbols.get_sp_500_nyc_yahoo_tickers()
    print(len(tickers)) 
    return tickers


tickers = getTicker()

db = mongo.get_collection2(DB_NAME, COLLECTION_NAME)
print(db)

for ticker in tickers:
    try:
        find = mongo.find_item_one(condition={"ticker": ticker }, db_name=DB_NAME, collection_name=COLLECTION_NAME)
        if find is None:
            item = yf.Ticker(ticker)
            stock = item.info
            stock['ticker'] = ticker
            id = db.insert_one(stock).inserted_id
            print(f'==> {ticker} is inserting ${id}')
        else:
            print(f'==> {ticker} is existed')

    except Exception as e:
        print(ticker, e)
        