import re


# --------------------------------------------------
# SKILLS
# --------------------------------------------------

JOB_SKILLS = [
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",

    "html",
    "css",
    "react",
    "node.js",

    "sql",
    "mysql",
    "postgresql",
    "mongodb",

    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",

    "pandas",
    "numpy",
    "scikit-learn",
    "tensorflow",
    "pytorch",

    "streamlit",

    "git",
    "github",
    "docker",

    "aws",
    "azure",
    "google cloud",

    "flask",
    "django",

    "power bi",
    "tableau"
]


# --------------------------------------------------
# JOB ROLE
# --------------------------------------------------

def extract_job_role(text):

    lines = text.splitlines()

    role_keywords = [
        "job title",
        "role",
        "position",
        "looking for",
        "hiring for"
    ]

    for line in lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        lower_line = clean_line.lower()

        for keyword in role_keywords:

            if keyword in lower_line:

                parts = re.split(
                    r":|-",
                    clean_line,
                    maxsplit=1
                )

                if len(parts) > 1:
                    return parts[1].strip()

    return None


# --------------------------------------------------
# REQUIRED SKILLS
# --------------------------------------------------

def extract_required_skills(text):

    text_lower = text.lower()

    found_skills = []

    for skill in JOB_SKILLS:

        if skill in text_lower:
            found_skills.append(skill)

    return found_skills


# --------------------------------------------------
# QUALIFICATIONS
# --------------------------------------------------

def extract_qualifications(text):

    lines = text.splitlines()

    qualifications = []

    keywords = [
        "qualification",
        "qualifications",
        "degree",
        "education",
        "bachelor",
        "b.tech",
        "btech",
        "master",
        "m.tech",
        "mtech"
    ]

    for line in lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        lower_line = clean_line.lower()

        if any(
            keyword in lower_line
            for keyword in keywords
        ):

            qualifications.append(clean_line)

    return qualifications


# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------

def extract_experience(text):

    patterns = [
        r"(\d+)\+?\s*years?\s+of\s+experience",
        r"(\d+)\+?\s*years?\s+experience",
        r"minimum\s+(\d+)\s+years?"
    ]

    text_lower = text.lower()

    for pattern in patterns:

        match = re.search(
            pattern,
            text_lower
        )

        if match:

            return (
                match.group(1)
                + " years"
            )

    return None


# --------------------------------------------------
# COMPLETE JOB PROCESSING
# --------------------------------------------------

def process_job_description(job_description):

    job_data = {

        "job_role": extract_job_role(
            job_description
        ),

        "required_skills": extract_required_skills(
            job_description
        ),

        "qualifications": extract_qualifications(
            job_description
        ),

        "experience": extract_experience(
            job_description
        )

    }

    return job_data