
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px


engine = create_engine("postgresql://postgres:tmv8NwFrKQUkOdWO@db.sgwlogdzejrgaoqvxuhc.supabase.co:5432/postgres")

st.title("Dashboard IoT")

df1 = pd.read_sql("SELECT * FROM avg_temp", engine)
st.plotly_chart(px.bar(df1, x="device_id", y="avg_temp"))

df2 = pd.read_sql("SELECT * FROM por_hora", engine)
st.plotly_chart(px.line(df2, x="hora", y="total"))

df3 = pd.read_sql("SELECT * FROM max_min", engine)
st.plotly_chart(px.line(df3, x="data", y=["max_temp","min_temp"]))
