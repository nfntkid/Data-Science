import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas_datareader as web
import mplfinance as mpf
import datetime as dt
import time
#cc = cryptocurrency

# store different cc's within a list
crypto = ["BTC","ETH"]
currency = "USD"

# set the start and end date for the graph then store the data
# for each cc in their respective variable
start = dt.datetime(2020,1,1)
end = dt.datetime.now()
btc = web.DataReader("{}-{}".format(crypto[0],currency), "yahoo", start, end)
eth = web.DataReader("{}-{}".format(crypto[1],currency), "yahoo", start, end)

# Use matplotlib to plot the opening prices only
plt.plot(btc["Open"])
#plt.show()

# Use matplotlib to plot the closing prices only
plt.plot(btc["Close"])
#plt.show()

# Plot the comparison between two cryptocurrencies such as bitcoin and ethereum
# Use a loarithmic scale to analyze drastic price change more closely
plt.yscale("log")
plt.plot(btc["Close"], label="BTC")
plt.plot(eth["Close"], label="ETH")
plt.legend(loc="upper left")
#plt.show()

# Plot a candle stick graph of the bitcoin opening and closing prices from
# the beginning of the year until now
mpf.plot(btc,type="candle",style="yahoo",volume=True)
