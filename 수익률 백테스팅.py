import streamlit as st
import FinanceDataReader as fdr

start_date = st.date_input('시작 날짜')
end_date = st.date_input('끝 날짜')

kospi_list = fdr.StockListing('KOSPI')

returns = {}
for symbol in kospi_list['Symbol']:
    df = fdr.DataReader(symbol, start_date, end_date)
    returns[symbol] = (df.iloc[-1]['Close'] - df.iloc[0]['Close']) / df.iloc[0]['Close']

for symbol, ret in returns.items():
    st.write(f"{symbol}의 수익률: {ret}")
