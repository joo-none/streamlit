import streamlit as st
import FinanceDataReader as fdr

kospi = fdr.StockListing('KOSPI')[['Code', 'Name', 'Close', 'Open', 'High', 'Low', 'Volume', 'Marcap']]
kospi100 = kospi.head(100)

st.set_page_config(
    page_title='수익률 백테스팅',
    page_icon="📈")

# sidebar - 기간
st.sidebar.header('종목을 선택하세요')

current_date = datetime.datetime.today().year

options = ['6개월', '1년', '5년']
selected_option = st.sidebar.selectbox('기간 선택', options)
if selected_option == '6개월':
    selected_date = current_date - timedelta(days=180)
elif selected_option == '1년':
    selected_date = current_date - timedelta(days=365)
elif selected_option == '5년':
    selected_Date = current_date - timedelta(days=1825)
    
# sidebar - 종목

item_list = kospi100['Name']
item_code = kospi100['Code']

tickers = kospi100.head(30)['Name'] # 코스피 상위 30 종목
seleced_ticker = st.sidebar.selectbox('Name', tickers)
    









# start_date = st.date_input('시작 날짜')
# end_date = st.date_input('끝 날짜')








# kospi_list = fdr.StockListing('KOSPI')

# returns = {}
# for symbol in kospi_list['Symbol']:
#     df = fdr.DataReader(symbol, start_date, end_date)
#     returns[symbol] = (df.iloc[-1]['Close'] - df.iloc[0]['Close']) / df.iloc[0]['Close']

# for symbol, ret in returns.items():
#     st.write(f"{symbol}의 수익률: {ret}")
