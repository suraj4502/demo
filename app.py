import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('vgsales.csv')
df['Publisher'].fillna('Unknown', inplace=True)

ts = df['Global_Sales'].sum()
tg = df.shape[0]
tp = len(df['Publisher'].unique())

st.sidebar.title("Sales Dashboard 📊.")
st.sidebar.markdown('---')

inp = st.sidebar.radio("Select Analysis.", ['Overview.',
                                            'Year wise Analyis.',
                                            'Genre wise Analysis.',
                                            'Platform wise Analysis.',
                                            'Publisher wise Analysis.'])

# overview

if inp == 'Overview.':
    st.title("Video Games Sales Analysis...🎮")
    st.markdown('---')

    col1, col2, col3 = st.columns([1, 1, 1])

    col1.metric("Tota Sales.", value=ts, delta="+")
    col2.metric("Total Games realeased.", value=tg, delta='+')
    col3.metric("TOtal Publishers.", value=tp, delta="+")

    st.markdown('---')

    st.image('game.png')

    st.header("Data Exploration.")
    st.markdown("""

       ---        
       #### *※ Columns in the data along with their description.*

       - `Rank:` The ranking position of the game in terms of global sales.
       - `Name:` The name of the video game.
       - `Platform:` The gaming platform (console or system) on which the game was released.
       - `Year:` The year when the game was released.
       - `Genre:` The genre or category of the game (e.g., action, adventure, sports).
       - `Publisher:` The company or entity responsible for publishing and distributing the game.
       - `NA_Sales:` Sales of the game in North America (in millions of units).
       - `EU_Sales:` Sales of the game in Europe (in millions of units).
       - `JP_Sales:` Sales of the game in Japan (in millions of units).
       - `Other_Sales:` Sales of the game in regions other than North America, Europe, and Japan (in millions of units).
       - `Global_Sales:` Total global sales of the game (sum of sales across all regions, in millions of units).
       ---
               """)

    st.header("data")
    st.dataframe(df)

    st.sidebar.markdown("---")
    games = df['Name'].unique()
    game = st.sidebar.selectbox('Select',games)

    temp = df[df['Name'] == game]

    btn = st.sidebar.button("Click")

    st.markdown('---')
    if btn:
        st.header(f"Info of {game}.")
        st.dataframe(temp)

elif inp == 'Year wise Analyis.':
    st.title("Yearwise Analysis.📅")

    st.header("Year wise Sales")
    temp = df.groupby("Year")['Global_Sales'].sum().reset_index()
    fig = px.line(temp, x="Year", y="Global_Sales")
    st.plotly_chart(fig)

    st.header("Games Released Per year.")
    temp = df['Year'].value_counts().sort_index()
    fig = px.bar(temp, x=temp.index, y=temp)
    st.plotly_chart(fig)


elif inp == 'Genre wise Analysis.':
    st.title("genre wise Analysis")

    temp = df['Genre'].value_counts().reset_index()

    fig = px.pie(temp, names='Genre', values="count",
                 hover_name='Genre', title="Genre Popularity",
                 height=700)
    st.plotly_chart(fig)

    st.header("Genre wise Sales.")
    temp = df.groupby('Genre')['Global_Sales'].sum()
    fig = px.bar(temp, x=temp.index, y=temp)
    st.plotly_chart(fig)


elif inp == 'Platform wise Analysis.':
    st.title("Platform Wise Analysis.")

    st.markdown("---")
    st.header("Genre Wise Sales.")
    temp = df.groupby('Platform')['Global_Sales'].sum().sort_values()
    fig = px.bar(temp, x=temp.index, y=temp)
    st.plotly_chart(fig)

    st.header("Best selling Game at every platform")
    temp = (df.groupby('Platform').
            apply(lambda x: x.nlargest(1, 'Global_Sales')).
            reset_index(drop=True))
    st.dataframe(temp[['Platform','Name']])


elif inp =='Publisher wise Analysis.':
    st.title("Publisher wise Analysis.")

    st.header("TOp PUBLISHERS.....")
    temp = (df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(10)
            .reset_index())

    fig= px.bar(temp, x="Publisher", y="Global_Sales")
    st.plotly_chart(fig)

    st.header("Contribution of Publishers.")
    fig = px.pie(temp, names='Publisher', values='Global_Sales', hover_name="Publisher")
    fig.update_layout(showlegend=False)
    st.plotly_chart(fig)