import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

fifa = pd.read_csv('fifa_eda.csv')

st.title("FIFA")

st.write('## Description')
st.write('This is thre description of the fifa project in streamlit')


st.subheader('top 5 valued players')
#st.dataframe(fifa.nlargest(5,'Value')[['Name','Value']])
                                                

col1,col2 = st.columns(2)

top5 = fifa.nlargest(5,'Value')[['Name','Value']]
top_players_dict = top5.set_index('Name').to_dict()

with col1:
    for Name, Value in top_players_dict['Value'].items():
        st.write(f'{Name}: {Value}')  
        
with col2:
    fig = px.bar(top5,x='Name', y='Value')
    st.plotly_chart(fig)
