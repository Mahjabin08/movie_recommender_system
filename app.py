import streamlit as st
import pickle
import pandas as pd
import requests



def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=f8b5332f92f5969ba77ac11596352062&language=en-US%27".format(movie_id))
    data = response.json()

    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]


def movie_recommend(movies):
    movie_index = movie[movie['title']==movies].index[0]
    movie_distances = movie_similarity[movie_index]
    movie_list= sorted(list(enumerate(movie_distances)), reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies_posters=[]
    recommended_movies=[]

    for i in movie_list:
       movie_id= movie.iloc[i[0]].movie_id

       recommended_movies.append(movie.iloc[i[0]].title)
        #fetch poster from streamlit API
       recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


movie_similarity = pickle.load(open("movie_similarity.pkl","rb"))
movie_list = pickle.load(open("movie_dict.pkl","rb"))
movie = pd.DataFrame(movie_list)

st.title("Movie Recommender System")

selected_movie = st.selectbox(
    'Enter the movie title',
    movie['title'].values)
if st.button('See similar movies'):
    names,posters = movie_recommend(selected_movie)
    # st.snow()

    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])