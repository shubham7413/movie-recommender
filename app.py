import streamlit as st
import pickle
import pandas as pd
import requests


def poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=252db21bdc5215fc63ebcdbdbeac87db&language=en-US'.format(
            movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500" + data['poster_path']


def recommendations(movie):
    index = movies[movies.title == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    r_movies = []
    movie_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        r_movies.append(movies.iloc[i[0]].title)
        movie_poster.append(poster(movie_id))
    return r_movies, movie_poster


movies_dictionary = pickle.load(open('mov_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dictionary)

st.title('Our MOVIE Recommendations :)')

movie_name = st.selectbox('Type your favourite movie name (and hope that it is in our database XD)',
                          movies.title.values)
st.text('We are pretty sure you will like these movies as well !! (Click below)')
if st.button('Click'):
    recommended_movie, recommended_poster = recommendations(movie_name)
    col1, col2 = st.columns(2)
    with col1:
        st.text(recommended_movie[0])
        st.image(recommended_poster[0])

    with col2:
        st.text(recommended_movie[1])
        st.image(recommended_poster[1])

    col1, col2 = st.columns(2)
    with col1:
        st.text(recommended_movie[2])
        st.image(recommended_poster[2])
    with col2:
        st.text(recommended_movie[3])
        st.image(recommended_poster[3])

    st.text(recommended_movie[4])
    st.image(recommended_poster[4])
