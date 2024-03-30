from flask import Flask, request, render_template
import pandas as pd
import re
from model import (load_data, preprocess_ratings_data, compute_tfidf_matrix,
                   compute_cosine_similarity, content_based_recommendations,
                   rank_movies_by_ratings)

app = Flask(__name__)

# Load data
movies_df, ratings_df = load_data("C:/Users/jaisw/Downloads/movies_.csv", "C:/Users/jaisw/Downloads/Ratings.csv")
ratings_df = preprocess_ratings_data(ratings_df)
tfidf_matrix = compute_tfidf_matrix(movies_df['Genres'])
cosine_sim = compute_cosine_similarity(tfidf_matrix)

# Function to search for partial matches in movie titles
def search_movie_titles(partial_title, movies_df):
    partial_title = partial_title.lower()
    matching_movies = movies_df[movies_df['Title'].str.lower().str.contains(partial_title)].copy()
    matching_movies['Title'] = matching_movies['Title'].apply(lambda x: re.sub(r'^(.*?),\s*The\s*\((\d{4})\)$', r'The \1 (\2)', x))
    return matching_movies

# Function to generate autocomplete suggestions for movie titles
def autocomplete(partial_title, movies_df):
    partial_title = partial_title.lower()
    matching_titles = movies_df[movies_df['Title'].str.lower().str.startswith(partial_title)].copy()
    matching_titles['Title'] = matching_titles['Title'].apply(lambda x: re.sub(r'^(.*?),\s*The\s*\((\d{4})\)$', r'The \1 (\2)', x))
    return matching_titles['Title'].tolist()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/recommendations', methods=['GET','POST'])
def get_recommendations():
    input_movie = request.form['movie_title']
    content_recs = content_based_recommendations(input_movie, cosine_sim, movies_df)
    ranked_movies = rank_movies_by_ratings(content_recs, ratings_df)
    top_recommendations = ranked_movies.head(10)
    return render_template('recommendations.html', recommendations=top_recommendations)

@app.route('/autocomplete', methods=['GET'])
def get_autocomplete():
    partial_title = request.args.get('partial_title')
    suggestions = autocomplete(partial_title, movies_df)[:10]
    return {'suggestions': suggestions}

if __name__ == '__main__':
    app.run(debug=True)
