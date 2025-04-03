import pandas as pd

#Load data
movies = pd.read_csv("D:\\SEM_3_STUDY\\Project\\archive (4)\\movie.csv")
rating = pd.read_csv("D:\\SEM_3_STUDY\Project\\archive (4)\\rating.csv")
tag = pd.read_csv("D:\\SEM_3_STUDY\\Project\\archive (4)\\tag.csv")

#Merge
merged_data = pd.merge(movies, rating, on='movieId')
full_data = pd.merge(merged_data, tag, on = ['userId', 'movieId'], how = "left")

print(full_data.head())