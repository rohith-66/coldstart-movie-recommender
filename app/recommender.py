import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(user_id):
    df = pd.read_csv("data/movielens_sample.csv")
    user_matrix = df.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)
    sim = cosine_similarity(user_matrix)
    similar_users = sim[user_id - 1].argsort()[::-1][1:6]
    recommended = user_matrix.iloc[similar_users].mean().sort_values(ascending=False).head(5)
    return recommended.index.tolist()

