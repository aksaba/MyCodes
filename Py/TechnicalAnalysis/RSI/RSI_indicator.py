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
ticker = pd.read_csv(r"D:\Github\MyCodes\Py\TechnicalAnalysis\RSI\ticker_above5000Cr.csv")
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
warnings.filterwarnings("ignore",category=pd.core.common.SettingWithCopyWarning)
start_date =  dt.datetime(2022, 2, 22, 5,30, 00)
start_date_unix = str(int(time.mktime(start_date.timetuple())))
end_date = dt.datetime(2023, 2, 22, 5, 30, 00)
end_date_unix = str(int(time.mktime(end_date.timetuple())))
interval = "1d"
# print(start_date_unix,"\n",end_date_unix)
#ticker = "INFY"
for count in range (0,len(ticker.ticker)):
    url_id="https://query1.finance.yahoo.com/v7/finance/download/"+ticker.ticker[count]+".NS"+"?period1="+start_date_unix+"&period2="+end_date_unix+"&interval="+interval+"&events=history&includeAdjustedClose=true"
    csv_file="D:\\Github\\MyCodes\\Py\\TechnicalAnalysis\\BuySignalCandle\\"+ticker.ticker[count]+".csv"
    output_csv="D:\\Github\\MyCodes\\Py\\TechnicalAnalysis\\BuySignalCandle\\"+ticker.ticker[count]+"_out.csv"
    output_png="D:\Github\\MyCodes\\Py\\TechnicalAnalysis\\BuySignalCandle\\"+ticker.ticker[count]+"_candle.png"
    # print(url_id)
    try:
        urllib.request.urlretrieve(url_id, csv_file)
    except HTTPError:
        print(" ")
    else:
        stock_prices = pd.read_csv(csv_file, index_col=0, parse_dates=True)
        # output = dict(fname="D:\InvestmentFundaAnal\Charting\\buysignal\\output.png",dpi=300)  # ,figsize=(1280/300))#pad_inches=0.5)
        # mpf.plot(stock_prices, type='candle', mav=(5, 20), volume=True, tight_layout=True, figratio=(10, 5), title="INFY",style='starsandstripes', savefig=output)
        stock_prices['RSI_7'] = ta.RSI(stock_prices['Close'], timeperiod=7)
        stock_prices['RSI_14'] = ta.RSI(stock_prices['Close'], timeperiod=14)
        stock_prices['RSI_21'] = ta.RSI(stock_prices['Close'], timeperiod=21)
        vol_max = stock_prices['Volume'].max()
        vol_min = stock_prices['Volume'].min()
        vol_avg = stock_prices['Volume'].mean()
        rsi_max_7=stock_prices['RSI_7'].max()
        rsi_min_7=stock_prices['RSI_7'].min()
        rsi_avg_7=stock_prices['RSI_7'].mean()
        rsi_max_14 = stock_prices['RSI_14'].max()
        rsi_min_14 = stock_prices['RSI_14'].min()
        rsi_avg_14 = stock_prices['RSI_14'].mean()
        rsi_max_21 = stock_prices['RSI_21'].max()
        rsi_min_21 = stock_prices['RSI_21'].min()
        rsi_avg_21 = stock_prices['RSI_21'].mean()
        # print(ticker.ticker[count],"\t",vol_avg,"\t",vol_max,"\t",vol_min,"\t",stock_prices.Volume[len(stock_prices['Volume'])-1],"\t",rsi_avg,"\t",rsi_max,"\t",rsi_min,"\t",stock_prices.RSI[len(stock_prices['Volume'])-1])
        stock_prices['rsi_indic_7'] = 0
        stock_prices['rsi_indic_14'] = 0
        stock_prices['rsi_indic_21'] = 0
        stock_prices['rsi_35_and_less'] = 0
        stock_prices['desc_ladder'] = 0
        low_rsi_freq = 0
        for check_count in range (0,len(stock_prices['RSI_7'])):
            if stock_prices.RSI_7[check_count] < (rsi_min_7 + (0.35*rsi_min_7)):
                # low_rsi_freq = low_rsi_freq + 1
                stock_prices.rsi_indic_7[check_count] = 1
        for check_count in range (0,len(stock_prices['RSI_14'])):
            if stock_prices.RSI_14[check_count] < (rsi_min_14 + (0.3*rsi_min_14)):
                # low_rsi_freq = low_rsi_freq + 1
                stock_prices.rsi_indic_14[check_count] = 1
        for check_count in range (0,len(stock_prices['RSI_21'])):
            if stock_prices.RSI_21[check_count] < (rsi_min_21 + (0.25*rsi_min_21)):
                # low_rsi_freq = low_rsi_freq + 1
                stock_prices.rsi_indic_21[check_count] = 1
        for check_count in range (0,len(stock_prices['RSI_7'])):
            if stock_prices.RSI_7[check_count] < 35:
                # low_rsi_freq = low_rsi_freq + 1
                stock_prices.rsi_35_and_less[check_count] = 1
        # print(ticker.ticker[count],"\t",len(stock_prices['Close']))
        for check_count in range(10, len(stock_prices['Close'])):
            if stock_prices.Close[check_count] < stock_prices.Close[check_count-1] and stock_prices.Close[check_count-1] < stock_prices.Close[check_count-2] and stock_prices.Close[check_count-2] < stock_prices.Close[check_count-3] and stock_prices.Close[check_count-3] < stock_prices.Close[check_count-4]:
                stock_prices.desc_ladder[check_count] = 1
        if len(stock_prices['Close']) > 200: #400:
            for check_count in range(len(stock_prices['RSI_7']) - 1,len(stock_prices['RSI_7']) - 2, -1):
                slope_minus1 = ((stock_prices.RSI_7[check_count] - stock_prices.RSI_7[check_count - 1]) /
                                stock_prices.RSI_7[check_count]) * 100
                slope_minus2 = ((stock_prices.RSI_7[check_count - 1] - stock_prices.RSI_7[check_count - 2]) /
                                stock_prices.RSI_7[check_count - 1]) * 100
                slope_minus3 = ((stock_prices.RSI_7[check_count - 2] - stock_prices.RSI_7[check_count - 3]) /
                                stock_prices.RSI_7[check_count - 2]) * 100
                if stock_prices.rsi_indic_7[check_count] == 1 or stock_prices.rsi_indic_14[check_count] == 1 or stock_prices.rsi_indic_21[check_count] == 1 or stock_prices.rsi_35_and_less[check_count] == 1 or stock_prices.desc_ladder[check_count] == 1:
                     # if stock_prices.RSI_4[check_count+1]>stock_prices.RSI_4[check_count] and stock_prices.RSI_14[check_count+1]>stock_prices.RSI_14[check_count] and stock_prices.RSI_21[check_count+1]>stock_prices.RSI_21[check_count]
                     #output = dict(fname=output_png, dpi=300)
                     #mpf.plot(stock_prices, type='candle', mav=(5, 20), volume=True, tight_layout=True,
                              # figratio=(10, 5), title=ticker.ticker[count], style='starsandstripes', savefig=output)
                     print(ticker.ticker[count],"\t",stock_prices.rsi_indic_7[check_count],"\t",stock_prices.rsi_indic_14[check_count],"\t",stock_prices.rsi_indic_21[check_count],"\t",stock_prices.rsi_35_and_less[check_count],"\t",stock_prices.desc_ladder[check_count],"\t",slope_minus3,"\t",slope_minus2,"\t",slope_minus1)
        #stock_prices.to_csv(output_csv, sep='\t', encoding='utf-8')
#indics = []
#data = yf.download("INFY",period="1y")#start="2021-01-01",end="2021-12-31")
#print(data)
#his_price = data.history(interval="1d")
#his_price
#indics['rsi'] = ta.RSI(data['Close'],timeperiod=14)
#print(indics)
