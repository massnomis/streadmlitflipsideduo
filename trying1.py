import streamlit as st
import plotly
import plotly.express as px
import statsmodels.api as sm
import pandas as pd
import json

# Basic setup and app layout
st.set_page_config(layout="wide")
st.title("bLUNA DEP")
st.markdown(
    """
    YEET
    """
)


st.header("BETHDEP")
query_id = "37eb9a7f-722f-41f0-8615-29084506abd1"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)
st.write(df)
st.write("TVL")

dai1 = px.line(
    df,
    x="DAY",
    y=["SUMDEPANC"]
  
)
st.plotly_chart(dai1, use_container_width=True)
dai2 = px.line(
    df,
    x="DAY",
    y=["COUNTS"]
  
)
st.plotly_chart(dai2, use_container_width=True)
dai3 = px.line(
    df,
    x="DAY",
    y=["AVGDEPANC"]
  
)
st.plotly_chart(dai3, use_container_width=True)
dai4 = px.line(
    df,
    x="DAY",
    y=["MEDDEPANC"]
  
)
st.plotly_chart(dai4, use_container_width=True)
# 	COUNTS	SUMDEPANC	AVGDEPANC	MEDDEPANC
# 	COUNT(TX_ID)	COUNT(DISTINCT(ORIGIN_ADDRESS))	SUM(AMOUNT)	AVG(AMOUNT)	MEDIAN(AMOUNT)

query_id = "06aefe77-45ae-4de2-b799-2b48cf8f87ac"
df = pd.read_json(
    f"https://api.flipsidecrypto.com/api/v2/queries/{query_id}/data/latest",
    convert_dates=["TIMESTAMP_NTZ"],
)   
dai2 = px.line(
    df,
    x="DAYZZ",
    y=["SUM(AMOUNT)"]
  
)
st.plotly_chart(dai2, use_container_width=True)
st.write(df)
dai2 = px.line(
    df,
    x="DAYZZ",
    y=["COUNT(TX_ID)"]
  
)
st.plotly_chart(dai2, use_container_width=True)
dai2 = px.line(
    df,
    x="DAYZZ",
    y=["COUNT(DISTINCT(ORIGIN_ADDRESS))"]
  
)
st.plotly_chart(dai2, use_container_width=True)
dai2 = px.line(
    df,
    x="DAYZZ",
    y=["MEDIAN(AMOUNT)"]
  
)
st.plotly_chart(dai2, use_container_width=True)
dai2 = px.line(
    df,
    x="DAYZZ",
    y=["AVG(AMOUNT)"]
  
)
st.plotly_chart(dai2, use_container_width=True)
# 

st.text('Fixed width text')
st.markdown('_Markdown_') # see *
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

st.caption('This is a small text')

