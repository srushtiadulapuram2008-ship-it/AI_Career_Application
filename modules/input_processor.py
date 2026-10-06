def process_inputs(
    uploaded_resume,
    job_description,
    skills,
    career_preferences
):
    data = {
        "resume": uploaded_resume,
        "job_description": job_description.strip(),
        "skills": skills.strip(),
        "career_preferences": career_preferences.strip()
    }

    return data