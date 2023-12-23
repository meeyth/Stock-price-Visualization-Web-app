import streamlit as st
from datetime import date

import yfinance as yf
from plotly import graph_objs as go


START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Visualization App")

stocks = ("RELIANCE.NS", "TCS.NS", "INFY.NS")

selected_stocks = st.selectbox("Select stock to visualize", stocks)



@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data


data_load_state = st.text("Load data...")
data = load_data(selected_stocks)
data_load_state.text("Loading data... Done!")

st.subheader("Raw data")
st.write(data.tail())

def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Open"], name="stock open", marker = {'color' : '#FF745C'}))
    fig.add_trace(go.Scatter(x=data["Date"], y=data["Close"], name="stock close", marker = {'color' : '#6C84F9'}))
    fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)
    pass
    
plot_raw_data()

