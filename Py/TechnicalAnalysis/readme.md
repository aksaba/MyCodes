These programs are used to perform technical analysis of stocks (or any other market entity).

There are various techniques involved in technical analysis. In these programs, we make use of two of those techniques.

1. Candlestick patters: The first, "buycandle.py" in the folder "BuySignalCandle", identifies predefined candlestick patters which could indicate a buy signal for a stock. 

2. Relative strength index (RSI): The second, "RSI_indicator.py" in the folder "RSI", makes use of the RSI indicator to identify oversold stocks. 

Both the programs make use of the functions available in the ta-lib library (https://www.ta-lib.org/). 

For the data, the yfinance library (https://pypi.org/project/yfinance/) is used to scrap and import the stock prices of a defined list of companies (in a csv file) that are listed in the NIFTY index.

Optionally, a candlestick chart can be plotted, which uses the mpl-finance library (https://pypi.org/project/mpl-finance/).

