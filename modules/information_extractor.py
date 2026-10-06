import re


# --------------------------------------------------
# EMAIL
# --------------------------------------------------

def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


# --------------------------------------------------
# PHONE
# --------------------------------------------------

def extract_phone(text):
    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return None


# --------------------------------------------------
# NAME
# --------------------------------------------------

def extract_name(text):

    lines = text.splitlines()

    ignored_words = [
        "resume",
        "curriculum vitae",
        "cv",
        "profile",
        "objective",
        "contact",
        "email",
        "phone"
    ]

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.lower() in ignored_words:
            continue

        if re.fullmatch(
            r"[A-Za-z]+(?:\s+[A-Za-z]+){1,4}",
            line
        ):
            return line

    return None


# --------------------------------------------------
# TECHNICAL SKILLS
# --------------------------------------------------

TECHNICAL_SKILLS = [
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


def extract_skills(text):

    text_lower = text.lower()

    found_skills = []

    for skill in TECHNICAL_SKILLS:

        if skill in text_lower:
            found_skills.append(skill)

    return found_skills


# --------------------------------------------------
# SECTION EXTRACTION
# --------------------------------------------------

def extract_section(text, section_names):

    lines = text.splitlines()

    collecting = False
    section_content = []

    stop_sections = [
        "skills",
        "technical skills",
        "education",
        "academic background",
        "projects",
        "experience",
        "work experience",
        "professional experience",
        "certifications",
        "certificates",
        "achievements",
        "contact",
        "profile",
        "objective"
    ]

    for line in lines:

        clean_line = line.strip()

        if not clean_line:
            continue

        lower_line = clean_line.lower()

        # Start section
        if lower_line in section_names:

            collecting = True
            continue

        # Stop at another section
        if collecting and lower_line in stop_sections:

            break

        if collecting:

            section_content.append(clean_line)

    return section_content


# --------------------------------------------------
# EDUCATION
# --------------------------------------------------

def extract_education(text):

    return extract_section(
        text,
        [
            "education",
            "academic background",
            "qualification",
            "qualifications"
        ]
    )


# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

def extract_projects(text):

    return extract_section(
        text,
        [
            "projects",
            "academic projects",
            "personal projects",
            "project"
        ]
    )


# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------

def extract_experience(text):

    return extract_section(
        text,
        [
            "experience",
            "work experience",
            "professional experience",
            "internship",
            "internships"
        ]
    )


# --------------------------------------------------
# CERTIFICATIONS
# --------------------------------------------------

def extract_certifications(text):

    return extract_section(
        text,
        [
            "certifications",
            "certificates",
            "certification",
            "certificate"
        ]
    )


# --------------------------------------------------
# COMPLETE INFORMATION EXTRACTION
# --------------------------------------------------

def extract_information(resume_text):

    information = {

        "name": extract_name(resume_text),

        "email": extract_email(resume_text),

        "phone": extract_phone(resume_text),

        "skills": extract_skills(resume_text),

        "education": extract_education(resume_text),

        "projects": extract_projects(resume_text),

        "experience": extract_experience(resume_text),

        "certifications": extract_certifications(resume_text)

    }

    return information