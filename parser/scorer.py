from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def calculate_match_score(text, keywords):
    vectorizer = CountVectorizer().fit_transform([text.lower(), " ".join(keywords)])
    score = cosine_similarity(vectorizer)[0][1]
    return round(score * 100, 2)

def estimate_experience_years(experience_list):
    years = 0.0
    for exp in experience_list:
        try:
            start = int(exp["Start"])
            end = int(exp["End"]) if exp["End"].lower() != "present" else 2025
            years += end - start
        except:
            continue
    return round(years, 1)
