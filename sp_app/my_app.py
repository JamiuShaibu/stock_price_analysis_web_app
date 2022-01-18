import streamlit as stl
import yfinance as yf
import pandas as pd
from datetime import date
from PIL import Image

# Display image in the web app
image = Image.open('global-markets.jpg')
stl.image(image, use_column_width=True)

stl.markdown("<h3 style='text-align: center; font:bold'>Simple Stock Price App</h3>", unsafe_allow_html=True)

# Recieve input of the stock name
stock_name = input("Enter Stock Name: ")
tickerSymbol = stock_name.strip().upper()

stl.write("""
***
Shown are the stock **closing price** and ***volume*** of """ + tickerSymbol)

# Get data on this ticker.
tickerData = yf.Ticker(tickerSymbol)
# To get to date historical prices of this ticker.
today = date.today()
# Get the historical prices of this ticker.
# Recieve input of Starting year.
start_year = input("\nEnter Starting Year in this format : YY-MM-DD; e.g 2000-1-1\nEnter Year : ")
# Recieve input of Ending year.
end_year = input("\nEnter Ending Year in this format : YY-MM-DD; e.g 2000-1-1\nEnter Year : ")

# Set Current date as default if ending year is not provided
if len(end_year) == 0:
    tickerDf = tickerData.history(period='1d', start=start_year, end=today)
    stl.write("""Showing """ + tickerSymbol, """Stock Price from: """ + start_year, """- Current Date""")
    stl.write("""**NOTE:** You didn't **enter** Targeted Closing Date. **Current Date is set as Default.**""")

elif len(start_year) == 0:
    # Set Default Starting year
    default_start = "2000-1-1"
    tickerDf = tickerData.history(period='1d', start=default_start, end=end_year)
    stl.write("""Showing """ + tickerSymbol, """Stock Price from: """ + default_start, """- """, end_year)
    stl.write("""**NOTE:** You didn't **enter** Targeted Starting Date. **Starting Date is set to 2000-1-1 as Default.**""")

elif len(start_year) == 0 and len(end_year) == 0:
    # Set Default
    start_from = "2000-1-1"
    tickerDf = tickerData.history(period='1d', start=start_from, end=today)
    stl.write("""Showing """ + tickerSymbol, """Stock Price from: """ + start_from, """- Current Date""")
    stl.write("""**NOTE:** You didn't **enter** Targeted Date for both Start and Close. **2000-1-1 and Current Date are set as Default.**""")

# Provide data within start_year and end_year
else:
    tickerDf = tickerData.history(period='1d', start=start_year, end=end_year)
    stl.write("""Showing """ + tickerSymbol, """Stock Price from: """ + start_year, """-""", end_year)
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
