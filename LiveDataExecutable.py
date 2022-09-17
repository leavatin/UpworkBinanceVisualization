import streamlit as st
import pandas as pd
import datetime as dt
from sqlalchemy import create_engine    
engine = create_engine('sqlite:///UpworkFinal.db')

st.title('Upwork Binance Live Data')

symbols = pd.read_sql('SELECT name FROM sqlite_master WHERE type = "table"', engine).name.tolist()

lookback = st.selectbox("Choose Timeframe", [1,15,30])

def qry(symbol, lookback):
    now = dt.datetime.utcnow()
    before = now - dt.timedelta(minutes=lookback)
    qry_str = f"""SELECT * FROM '{symbol}' WHERE time >= '{before}'"""
    df = pd.read_sql(qry_str, engine)
    return df

def return_calc(df):
    cum_ret = (df.price.pct_change() + 1).prod() - 1
    return cum_ret  

def allreturns():
    returns = []
    for symbol in symbols:
        returns.append(return_calc(qry(symbol, lookback)))
    return returns

if st.button('Update'):
    allreturns()

all_ret = pd.DataFrame(allreturns(), symbols, columns=['Performance'])

top = all_ret.Performance.nlargest(20)

worst = all_ret.Performance.nsmallest(20)

cols = st.columns(2)

cols[0].title('Top Performer')
cols[0].write(top)
cols[1].title('Worst Performer')
cols[1].write(worst)
    