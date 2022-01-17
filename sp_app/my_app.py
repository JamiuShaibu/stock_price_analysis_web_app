import streamlit as stl
import yfinance as yf
import pandas as pd
from datetime import date
from PIL import Image


image = Image.open('global-markets.jpg')
stl.image(image, use_column_width=True)

stl.markdown("<h3 style='text-align: center; font:bold'>Simple Stock Price App</h3>", unsafe_allow_html=True)


# Stock list = [GOOGL, AAPL]
# Define the ticker Symbol.
tickerSymbol = 'AAPL'

stl.write("""
***
Shown are the stock **closing price** and ***volume*** of """ + tickerSymbol)

# Get data on this ticker.
tickerData = yf.Ticker(tickerSymbol)
# To get to date historical pricesof this ticker.
today = date.today()
# Get the historical prices of this ticker.
tickerDf = tickerData.history(period='1d', start='2019-1-1', end=today)
# Open   High   Low   Close Volume  Dividends   Stock  Splits.

stl.markdown("<h5 style='text-align: left; color: navy'>Closing Price</h5>", unsafe_allow_html=True)
# stl.write("""
# ## Closing Price
# """)
stl.line_chart(tickerDf.Close)

stl.markdown("<h5 style='text-align: left; color: navy'>Volume Price</h5>", unsafe_allow_html=True)
# stl.write("""
# ## Volume Price
# """)
stl.line_chart(tickerDf.Volume)

stl.markdown("<h6 style='text-align: center;'>A stock price is a given for every share issued by a publicly traded company. The price is a reflection of the company’s value – what the public is willing to pay for a piece of the company. It can and will rise and fall, based on a variety of factors in the global landscape and within the company itself.</h6>", unsafe_allow_html=True)


stl.markdown("<h6 style='text-align: right; color: navy '>By; Jamiu Shaibu</h6>", unsafe_allow_html=True)


# stl.markdown("<h6 style='text-align: center; font:bold'>This app was built by Jamiu Shaibu, an app that counts the nucleotide composition of query DNA.</h6>", unsafe_allow_html=True)
