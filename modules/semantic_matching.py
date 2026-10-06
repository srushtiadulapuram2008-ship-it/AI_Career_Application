from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_semantic_similarity(resume_text, job_description):
    if not resume_text.strip() or not job_description.strip():
        return 0.0

    documents = [
        resume_text.lower(),
        job_description.lower()
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    score = round(similarity * 100, 2)

    return score


def get_similarity_level(score):
    if score >= 75:
        return "Excellent Match"
    elif score >= 50:
        return "Good Match"
    elif score >= 30:
        return "Moderate Match"
    else:
        return "Low Match"


def semantic_match(resume_text, job_description):
    score = calculate_semantic_similarity(
        resume_text,
        job_description
    )

    level = get_similarity_level(score)

    return {
        "semantic_score": score,
        "similarity_level": level
    }