import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity

# Load data
movies = pd.read_csv("D:\\SEM_3_STUDY\\Project\\archive (4)\\movie.csv")
rating = pd.read_csv("D:\\SEM_3_STUDY\\Project\\archive (4)\\rating.csv")
tag = pd.read_csv("D:\\SEM_3_STUDY\\Project\\archive (4)\\tag.csv")
genome_scores = pd.read_csv("D:\\SEM_3_STUDY\\Project\\archive (4)\\genome_scores.csv")
genome_tags = pd.read_csv("D:\\SEM_3_STUDY\\Project\\archive (4)\\genome_tags.csv")
links = pd.read_csv("D:\\SEM_3_STUDY\\Project\\archive (4)\\link.csv")

# Clean data
rating['timestamp'] = pd.to_datetime(rating['timestamp'], errors='coerce')
rating.dropna(subset=['timestamp'], inplace=True)

# ❌ This line had a typo: movies.drratings_with_movies = ...
# ✅ Correct it:
ratings_with_movies = pd.merge(rating, movies, on='movieId')

# Filter most active users and popular movies
active_users = ratings_with_movies['userId'].value_counts().loc[lambda x: x > 20].index
popular_movies = ratings_with_movies['title'].value_counts().loc[lambda x: x > 10].index

filtered_ratings = ratings_with_movies[
    ratings_with_movies['userId'].isin(active_users) &
    ratings_with_movies['title'].isin(popular_movies)
]

# Pivot safely
user_movie_matrix = filtered_ratings.pivot_table(index='userId', columns='title', values='rating')
user_movie_matrix.fillna(0, inplace=True)

# Normalize
scaler = StandardScaler()
user_movie_matrix_scaled = scaler.fit_transform(user_movie_matrix)


# ✅ Fix: convert back to DataFrame before saving
user_movie_matrix_scaled_df = pd.DataFrame(user_movie_matrix_scaled, index=user_movie_matrix.index, columns=user_movie_matrix.columns)
user_movie_matrix_scaled_df.to_csv("D:\\SEM_3_STUDY\\Project\\archive (4)\\output_files.csv")
