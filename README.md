# coldstart-movie-recommender
Hybrid recommender using OpenAI embeddings and collaborative filtering to tackle the cold-start problem.

# Cold-Start Movie Recommender using LLM Embeddings

This project solves the cold-start problem in movie recommendation using a hybrid approach. It combines LLM-based semantic embeddings from OpenAI with collaborative filtering techniques to provide relevant recommendations even for new or sparse user profiles.

## Tech Stack
- **Backend:** Python, FastAPI, Scikit-learn
- **Frontend:** React.js
- **ML Models:** OpenAI Embeddings + User-Item Collaborative Filtering
- **Similarity:** Cosine Similarity for re-ranking
- **Deployment:** Docker

## Dataset
- MovieLens 100k sample
- Stored under `data/movielens_sample.csv`

## Features
- LLM-encoded movie descriptions to enhance recommendations
- Cold-start handling for new users/items
- REST API endpoint to fetch top-N movie recommendations
- Lightweight React frontend for user interface

## Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/coldstart-movie-recommender.git
cd coldstart-movie-recommender

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload
