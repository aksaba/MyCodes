import mplfinance as mpf
import pandas as pd
import urllib.request
from urllib.error import HTTPError
import warnings
import matplotlib.cbook
import matplotlib.pyplot as plt
import talib as ta
import yfinance as yf
import datetime as dt
import time
ticker = pd.read_csv(r"D:\Github\MyCodes\Py\TechnicalAnalysis\BuySignalCandle\ticker_above5000Cr.csv")
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
start_date =  dt.datetime(2023, 1, 25, 5,30, 00)
start_date_unix = str(int(time.mktime(start_date.timetuple())))
end_date = dt.datetime(2023, 2, 13, 5, 30, 00)
end_date_unix = str(int(time.mktime(end_date.timetuple())))
interval = "1d"
# print(start_date_unix,"\n",end_date_unix)
#ticker = "INFY"
for count in range (0,len(ticker.ticker)):
    url_id="https://query1.finance.yahoo.com/v7/finance/download/"+ticker.ticker[count]+".NS"+"?period1="+start_date_unix+"&period2="+end_date_unix+"&interval="+interval+"&events=history&includeAdjustedClose=true"
    csv_file="D:\\Github\\MyCodes\\Py\\TechnicalAnalysis\\BuySignalCandle\\input\\"+ticker.ticker[count]+".csv"
    output_csv="D:\\Github\\MyCodes\\Py\\TechnicalAnalysis\\BuySignalCandle\\output\\"+ticker.ticker[count]+"_out.csv"
    # print(url_id)
    try:
        urllib.request.urlretrieve(url_id, csv_file)
    except HTTPError:
        print("Something bad happened with", ticker.ticker[count])
    else:
        stock_prices = pd.read_csv(csv_file, index_col=0, parse_dates=True)
        stock_prices['maru'] = ta.CDLMARUBOZU(stock_prices['Open'],stock_prices['High'],stock_prices['Low'],stock_prices['Close'])
        stock_prices['hamm'] = ta.CDLHAMMER(stock_prices['Open'],stock_prices['High'],stock_prices['Low'],stock_prices['Close'])
        stock_prices['mstar'] = ta.CDLMORNINGSTAR(stock_prices['Open'],stock_prices['High'],stock_prices['Low'],stock_prices['Close'],penetration=0)
        stock_prices['bladder'] = ta.CDLLADDERBOTTOM(stock_prices['Open'],stock_prices['High'],stock_prices['Low'],stock_prices['Close'])
        stock_prices['kick'] = ta.CDLKICKING(stock_prices['Open'],stock_prices['High'],stock_prices['Low'],stock_prices['Close'])
        stock_prices['doji'] = ta.CDLDOJI(stock_prices['Open'],stock_prices['High'],stock_prices['Low'],stock_prices['Close'])
        for check_count in range (len(stock_prices.maru)-1,len(stock_prices.maru)-2,-1):
            #print(stock_prices.maru[check_count])
            if stock_prices.maru[check_count] == 100:
                maru_length=((stock_prices.Close[check_count]-stock_prices.Open[check_count])/stock_prices.Open[check_count])*100
                print(ticker.ticker[count],"\t","Maru","\t",stock_prices.index[check_count])
                #stock_prices.to_csv(url.outputcsv[count], sep='\t', encoding='utf-8')
            elif stock_prices.hamm[check_count] == 100:
                 print(ticker.ticker[count], "\t","Hamm","\t",stock_prices.index[check_count])
            elif stock_prices.mstar[check_count] == 100:
                print(ticker.ticker[count], "\t", "Mstar", "\t", stock_prices.index[check_count])
            elif stock_prices.bladder[check_count] == 100:
                print(ticker.ticker[count], "\t", "Ladder bottom","\t",stock_prices.index[check_count])
            elif stock_prices.kick[check_count] == 100:
                print(ticker.ticker[count], "\t", "kick", "\t", stock_prices.index[check_count])
        # for check_count in range(len(stock_prices.maru) - 2, len(stock_prices.maru) - 3, -1):
        #     if stock_prices.doji[check_count] == 100 and (stock_prices.Close[check_count+1]>stock_prices.Open[check_count+1]):
        #         print(ticker.ticker[count], "\t", "doji", "\t", stock_prices.index[check_count])
