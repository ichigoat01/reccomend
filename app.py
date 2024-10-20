import streamlit as st
import pickle
import pandas as pd

def reccomend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)) , reverse=True , key = lambda x:x[1])[1:6]

    reccomended_movies = []
    for i in movies_list:
        reccomended_movies.append(movies.iloc[i[0]].title)
    return reccomended_movies


st.title('Movie Reccomender System')
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

selected_movie_name = st.selectbox(
    'Choose a Movie for Reccomendations' ,
    movies['title'].values
)

if st.button('Reccomend'):
    reccomendations = reccomend(selected_movie_name)
    for i in reccomendations:
        st.write(i)