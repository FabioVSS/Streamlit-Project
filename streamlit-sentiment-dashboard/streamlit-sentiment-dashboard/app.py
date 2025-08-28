import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

Data_URL = ('Tweets.csv')

st.title('Sentiment Analyses of Tweets about US Airlines')
st.sidebar.title('Sentiment Analyses of Tweets')
st.markdown('This aplication is a Streamlit dasboard used ' \
            'to analyze sentiments of tweets')
st.sidebar.markdown('This apllication is a Streamlit dashboard used to analyse sentiments of tweets')

@st.cache_data(persist=True)
def load_data():
    data = pd.read_csv(Data_URL)
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data

data = load_data()

st.sidebar.subheader("Show random tweet")
random_tweet = st.sidebar.radio('Sentiment', list(data['airline_sentiment'].drop_duplicates()))
st.sidebar.markdown(data.query('airline_sentiment == @random_tweet')[['text']].sample(n=1).iat[0,0])

st.sidebar.markdown('### Number of tweets by sentiment')
select = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'], key='1')
sentiment_count = data['airline_sentiment'].value_counts()
sentiment_count = pd.DataFrame({'Sentiment':sentiment_count.index, 'Tweets':sentiment_count.values})
if not st.sidebar.checkbox('Hide', True):
    st.markdown('### Number of tweets by sentiment')
    if select == 'Bar plot':
        fig = px.bar(sentiment_count,
                    x='Sentiment',
                    y='Tweets',
                    color=['#3D553E', '#6D7F6E', '#9EAA9E'],
                    color_discrete_map="identity",
                    height=500,
                    text_auto='.2s'
                    )
        fig.update_traces(textfont_size=15, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig)
    else:
        fig =px.pie(
                    sentiment_count,
                    values='Tweets',
                    names='Sentiment',
                    color_discrete_sequence= ['#3D553E', '#6D7F6E', '#9EAA9E']
                    )
        fig.update_traces(hole=.4)
        st.plotly_chart(fig)
st.sidebar.subheader('When and where are users tweeting from?')
hour = st.sidebar.slider('Hour to look at', 0, 23)
modified_data = data[data['tweet_created'].dt.hour == hour]
if not st.sidebar.checkbox('Close', True):
    st.markdown('### Tweet locations based on time of day')
    st.markdown('%i tweets between %i:00 and %i:00' % (len(modified_data), hour, (hour + 1)% 24))
    st.map(modified_data, color='#3D553E')
    if st.sidebar.checkbox('Show raw data', False):
        st.write(modified_data)

st.sidebar.subheader('Total number of tweets for each airline')
each_airline = st.sidebar.selectbox('Visualization type', ['Bar plot', 'Pie chart'])
airline_sentiment_count = data.groupby('airline')['airline_sentiment'].count().sort_values(ascending=False)
airline_sentiment_count = pd.DataFrame({'Airline': airline_sentiment_count.index, 'Tweets': airline_sentiment_count.values})
if not st.sidebar.checkbox('Close', True, key='2'):
    if each_airline == 'Bar plot':
        st.subheader('Total number of tweets for each airline')
        fig_1 = px.bar(
                        airline_sentiment_count,
                        x= 'Tweets',
                        y='Airline',
                        height=500,
                        orientation='h',
                        color=['#042B0B', '#263F26', '#3D553E','#546955' ,'#6D7F6E', '#9EAA9E'] ,
                        color_discrete_map='identity',
                        text_auto='.2s'
                        )
        fig_1.update_traces(textfont_size=15, textposition="outside", cliponaxis=False)
        st.plotly_chart(fig_1)
    if each_airline == 'Pie chart':
        st.subheader('Total number of tweets for each airline')
        fig_2 = px.pie(
                        airline_sentiment_count,
                        values='Tweets',
                        names='Airline',
                        color_discrete_sequence=['#042B0B', '#263F26', '#3D553E','#546955' ,'#6D7F6E', '#9EAA9E']
                        )
        st.plotly_chart(fig_2)

@st.cache_data(persist=True)
def plot_sentiment(airline):
    df = data[data['airline']==airline]
    count = df['airline_sentiment'].value_counts()
    count = pd.DataFrame({'Sentiment':count.index, 'Tweets':count.values})
    return count

st.sidebar.subheader('Breakdown airlineby sentiment')
choice = st.sidebar.multiselect('Pick airlines', (list(data['airline'].drop_duplicates())))
if len(choice)> 0:
    choice_data = data[data.airline.isin(choice)]
    fig_0 = px.histogram(
                        choice_data, x='airline',
                        y='airline_sentiment',
                        histfunc='count',
                        facet_col='airline_sentiment',
                        labels={'airline_sentiment':'Tweets'},
                        height=600,
                        width=800,
                        color= ['#042B0B', '#263F26', '#3D553E','#546955' ,'#6D7F6E', '#9EAA9E'],
                        color_discrete_map="identity"
                        )
    fig_0.update_traces(textfont_size=15, textposition="outside", cliponaxis=False)
    st.plotly_chart(fig_0)

st.sidebar.header('Word Cloud')
word_sentiment = st.sidebar.radio('Display word cloud for what sentiment?', ('postive', 'neutral', 'negative'))
if not st.sidebar.checkbox("Close", True, key='3'):
    st.subheader('Word cloud for %s sentiment' %(word_sentiment))
    df = data[data['airline_sentiment']== word_sentiment].reset_index(drop=True)
    text = df.text[0]
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()