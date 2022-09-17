import requests
import streamlit as sl
import pickle
import pandas as pd


def poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{'
                            '}?api_key=fc0d462afc1fe23d057b8dc1fd4412c3&language=en-US'.format(movie_id))
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']


def recommend(movie):
    Index = movies[movies['title'] == movie].index[0]
    Distance = similarity[Index]
    List = sorted(list(enumerate(Distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies_names = []
    recommended_movies_posters = []
    for i in List:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_names.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(poster(movie_id))
    return recommended_movies_names, recommended_movies_posters


similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_list = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

sl.title('Movie Recommendation System')

selected_movie = sl.selectbox(
    "Type the name of your movie",
    movies['title'].values
)

if sl.button('Recommend'):
    names, posters = recommend(selected_movie)

    c1, c2, c3, c4, c5 = sl.columns(5)

    with c1:
        sl.text(names[0])
        sl.image(posters[0])

    with c2:
        sl.text(names[1])
        sl.image(posters[1])

    with c3:
        sl.text(names[2])
        sl.image(posters[2])

    with c4:
        sl.text(names[3])
        sl.image(posters[3])

    with c5:
        sl.text(names[4])
        sl.image(posters[4])

# to run the code write 'streamlit run App.py' in terminal
