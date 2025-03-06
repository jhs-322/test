import streamlit as st
import datetime
import pyupbit


d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today()
)

st.write('비트코인 1일 차트')

ticker = 'KRW-BTC'
interval = 'minute60'
to = str(d+datetime.timedelta(days=1)) #어디까지 업데이트
count = 24 #24시간
price_now = pyupbit.get_ohlcv(ticker= ticker, interval=interval, count=count, to=to)
st.line_chart(price_now.close)

