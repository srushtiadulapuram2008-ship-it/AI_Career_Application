# --------------------------------------------------
# SKILL MATCHING
# --------------------------------------------------

def normalize_skill(skill):
    return skill.strip().lower()


def find_matching_skills(resume_skills, job_skills):

    resume_set = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    job_set = {
        normalize_skill(skill)
        for skill in job_skills
    }

    matched = resume_set.intersection(job_set)

    return sorted(matched)


def find_missing_skills(resume_skills, job_skills):

    resume_set = {
        normalize_skill(skill)
        for skill in resume_skills
    }

    job_set = {
        normalize_skill(skill)
        for skill in job_skills
    }

    missing = job_set - resume_set

    return sorted(missing)


def calculate_match_score(resume_skills, job_skills):

    if not job_skills:
        return 0

    matched_skills = find_matching_skills(
        resume_skills,
        job_skills
    )

    score = (
        len(matched_skills)
        / len(job_skills)
    ) * 100

    return round(score, 2)


def match_resume_with_job(
    resume_skills,
    job_skills
):

    matched_skills = find_matching_skills(
        resume_skills,
        job_skills
    )

    missing_skills = find_missing_skills(
        resume_skills,
        job_skills
    )

    match_score = calculate_match_score(
        resume_skills,
        job_skills
    )

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": match_score
    }