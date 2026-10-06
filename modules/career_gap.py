def calculate_gap_percentage(required_skills, missing_skills):
    if not required_skills:
        return 0

    gap = (len(missing_skills) / len(required_skills)) * 100

    return round(gap, 2)


def identify_skill_priority(skill):
    high_priority = [
        "python",
        "java",
        "c++",
        "machine learning",
        "artificial intelligence",
        "data science",
        "sql",
        "deep learning"
    ]

    medium_priority = [
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "react",
        "javascript",
        "docker",
        "aws",
        "azure"
    ]

    if skill.lower() in high_priority:
        return "High"

    if skill.lower() in medium_priority:
        return "Medium"

    return "Low"


def generate_career_gap(required_skills, missing_skills):
    gap_percentage = calculate_gap_percentage(
        required_skills,
        missing_skills
    )

    missing_skill_details = []

    for skill in missing_skills:
        priority = identify_skill_priority(skill)

        missing_skill_details.append({
            "skill": skill,
            "priority": priority
        })

    if gap_percentage <= 20:
        gap_level = "Small Career Gap"
    elif gap_percentage <= 50:
        gap_level = "Moderate Career Gap"
    else:
        gap_level = "Large Career Gap"

    return {
        "gap_percentage": gap_percentage,
        "gap_level": gap_level,
        "missing_skill_details": missing_skill_details
    }