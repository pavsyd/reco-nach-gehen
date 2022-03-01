import yfinance as yf
import streamlit as st
import pandas as pd

st.header('Russian Economy, go nach...')

# Stocks
st.text('''Stocks 
Котирування акцій рос. компаній''')

tickers = yf.Tickers('OGZPY LUKOY NILSY YNDX GZPFY SBRCY OAOFY')
tickers_df = tickers.history(start='2022-02-01')
st.line_chart(tickers_df.Open)

# ETF
st.text('''VanEck Vectors Russia ETF 
Котирування інвест. фонду, який спеціалізується на російських акціях''')

rsx = yf.Ticker('RSX')
rsx_df = rsx.history(start='2022-02-01')
st.area_chart(rsx_df.Close)

# USD/RUB data
st.text('''USD/RUB 
Обмінний курс рубля до дол. США''')

rub = yf.Ticker('RUB=X')
rub_df = rub.history(start='2022-02-01')
st.line_chart(rub_df.Close)

st.write('Source: yahoo!finance')