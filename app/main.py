from recommender import get_recommendations

if __name__ == "__main__":
    user_id = 1
    recommendations = get_recommendations(user_id)
    print("Recommended movies:", recommendations)

