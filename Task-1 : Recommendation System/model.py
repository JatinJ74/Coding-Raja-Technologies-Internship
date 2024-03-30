import pandas as pd
import re
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def load_data(movie_data_path, ratings_data_path):
    movies_df = pd.read_csv(movie_data_path)
    ratings_df = pd.read_csv(ratings_data_path)
    return movies_df, ratings_df

def preprocess_ratings_data(ratings_df):
    ratings_df.replace([np.inf, -np.inf], np.nan, inplace=True)
    ratings_df['Rating'] = pd.to_numeric(ratings_df['Rating'], errors='coerce')
    ratings_df['Rating'].fillna(ratings_df['Rating'].mean(), inplace=True)
    ratings_df['Rating'] = ratings_df['Rating'].astype(int)
    return ratings_df

def compute_tfidf_matrix(data):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data)
    return tfidf_matrix

def compute_cosine_similarity(tfidf_matrix):
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    return cosine_sim

# def content_based_recommendations(movie_title, cosine_sim, movies_df):
#     idx = movies_df.index[movies_df['Title'] == movie_title].tolist()[0]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:11]  # Top 10 similar movies
#     movie_indices = [i[0] for i in sim_scores]
#     recommended_movies = movies_df.iloc[movie_indices].copy()
#     return recommended_movies

def content_based_recommendations(movie_title, cosine_sim, movies_df):
    idx = movies_df.index[movies_df['Title'] == movie_title].tolist()

    if not idx:
        return None  # Return None if the movie is not found in the dataset

    idx = idx[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]  # Top 10 similar movies
    movie_indices = [i[0] for i in sim_scores]

    # Create DataFrame with recommended movies
    recommended_movies = movies_df.iloc[movie_indices].copy()

    # Check if input movie is already in recommended list, if not, append it
    if idx not in recommended_movies.index:
        input_movie_row = pd.DataFrame(movies_df.iloc[idx]).T
        recommended_movies = pd.concat([input_movie_row, recommended_movies])

    return recommended_movies


def rank_movies_by_ratings(recommended_movies, ratings_df):
    recommended_with_ratings = pd.merge(recommended_movies, ratings_df, on='MovieID')
    movie_ratings = np.round(recommended_with_ratings.groupby('Title')['Rating'].mean(),2).reset_index()
    movie_ratings['Title'] = movie_ratings['Title'].apply(lambda x: re.sub(r'^(.*?),\s*The\s*\((\d{4})\)$', r'The \1 (\2)', x))
    ranked_movies = movie_ratings.sort_values(by=['Rating', 'Title'], ascending=[False, True])
    ranked_movies['Rank'] = range(1, len(ranked_movies) + 1)
    return ranked_movies
