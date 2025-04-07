import numpy as np
imp

ratings = np.array([
    [5, 3, np.nan],
    [4, 2, 4],
    [1, 5, 2]
])

def cosine_sim(a, b):
    mask = ~np.isnan(a) & ~np.isnan(b)
    a_filtered = a[mask]
    b_filtered = b[mask]

    if len(a_filtered) == 0:
        return 0

    dot_product = np.dot(a_filtered, b_filtered)
    norm_a = np.linalg.norm(a_filtered)
    norm_b = np.linalg.norm(b_filtered)

    if norm_a == 0 or norm_b == 0:
        return 0

    return dot_product / (norm_a * norm_b)

num_movies = ratings.shape[1]
similarity_matrix = np.zeros((num_movies, num_movies))

for i in range(num_movies):
    for j in range(num_movies):
        movie_i = ratings[:, i]
        movie_j = ratings[:, j]
        similarity_matrix[i, j] = cosine_sim(movie_i, movie_j)

print("Cosine similarity matrix (with NaN handled):")
print(np.round(similarity_matrix, 4))


# --- Predict missing value for User1 → Movie C (index 0, 2) ---

user_index = 0
target_movie = 2  # Movie C

numerator = 0
denominator = 0

for other_movie in range(num_movies):
    if other_movie == target_movie:
        continue  # skip comparing movie with itself

    user_rating = ratings[user_index, other_movie]
    if np.isnan(user_rating):
        continue  # skip if user didn't rate this movie

    similarity = similarity_matrix[target_movie, other_movie]  # similarity between C and A or B

    numerator += similarity * user_rating
    denominator += abs(similarity)

# Calculate predicted rating
if denominator == 0:
    predicted_rating = np.nan
else:
    predicted_rating = numerator / denominator

print(f"\n✅ Predicted rating for User1 → Movie C: {round(predicted_rating, 4)}")
print("Understood")

print("Hello Mayur, Kavin")
