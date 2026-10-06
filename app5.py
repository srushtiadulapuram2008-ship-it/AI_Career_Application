import streamlit as st

from modules.input_processor import process_inputs

from modules.resume_parser import (
    extract_resume_text,
    clean_resume_text
)

from modules.information_extractor import (
    extract_information
)

from modules.job_processor import (
    process_job_description
)
from modules.matching import match_resume_with_job
from modules.semantic_matching import semantic_match
from modules.career_gap import generate_career_gap

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Career Application",
    page_icon="🎯",
    layout="wide"
)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎯 AI-Powered Career Application")

st.write(
    "Upload your resume and provide job-related information "
    "to analyze your career profile."
)


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.header("📥 Enter Your Details")


uploaded_resume = st.file_uploader(
    "Upload Resume (PDF or DOCX)",
    type=["pdf", "docx"]
)


job_description = st.text_area(
    "💼 Job Description",
    placeholder="Paste the job description here...",
    height=180
)


skills = st.text_input(
    "🛠️ Your Skills",
    placeholder="Example: Python, SQL, Machine Learning, Java"
)


career_preferences = st.text_area(
    "🎯 Career Preferences",
    placeholder="Example: I want to work in AI/ML and software development.",
    height=120
)


# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------

if st.button("🔍 Analyze Resume", use_container_width=True):

    # --------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------

    if uploaded_resume is None:
        st.error("❌ Please upload your resume.")
        st.stop()

    if not job_description.strip():
        st.error("❌ Please enter the job description.")
        st.stop()

    if not skills.strip():
        st.error("❌ Please enter your skills.")
        st.stop()

    if not career_preferences.strip():
        st.error("❌ Please enter your career preferences.")
        st.stop()


    # --------------------------------------------------
    # PHASE 1: PROCESS INPUTS
    # --------------------------------------------------

    career_data = process_inputs(
        uploaded_resume,
        job_description,
        skills,
        career_preferences
    )


    st.success("✅ All inputs received successfully.")


    # --------------------------------------------------
    # PHASE 2: RESUME TEXT EXTRACTION
    # --------------------------------------------------

    try:

        resume_text = extract_resume_text(
            career_data["resume"]
        )

        resume_text = clean_resume_text(
            resume_text
        )

    except Exception as e:

        st.error(
            f"❌ Could not extract resume text: {e}"
        )

        st.stop()


    # --------------------------------------------------
    # PHASE 3: RESUME INFORMATION EXTRACTION
    # --------------------------------------------------

    try:

        resume_info = extract_information(
            resume_text
        )

    except Exception as e:

        st.error(
            f"❌ Could not extract resume information: {e}"
        )

        st.stop()


    # --------------------------------------------------
    # PHASE 4: JOB DESCRIPTION PROCESSING
    # --------------------------------------------------

    try:

        job_data = process_job_description(
            career_data["job_description"]
        )
        # -----------------------------
        # PHASE 5: MATCHING
        # -----------------------------

        match_data = match_resume_with_job(
            resume_info["skills"],
            job_data["required_skills"]
            )
        # -----------------------------
        # MATCHING RESULTS
        # -----------------------------

        st.subheader("📊 Resume ↔ Job Matching")


        # Match Score
        st.metric(
            "🎯 Overall Match Score",
            f"{match_data['match_score']}%"
            )


        # Matched Skills
        st.write("✅ **Matched Skills:**")
        if match_data["matched_skills"]:
            for skill in match_data["matched_skills"]:
                st.write(f"• {skill}")
        else:
            st.write("No matching skills found.")


        # Missing Skills
        st.write("❌ **Missing Skills:**")
        if match_data["missing_skills"]:
            for skill in match_data["missing_skills"]:
                st.write(f"• {skill}")
        else:
            st.write("🎉 No required skills are missing!")
        

    except Exception as e:

        st.error(
            f"❌ Could not process job description: {e}"
        )

        st.stop()


    # --------------------------------------------------
    # DISPLAY RESUME TEXT
    # --------------------------------------------------

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=400
    )


    # --------------------------------------------------
    # DISPLAY RESUME INFORMATION
    # --------------------------------------------------

    st.subheader("📋 Extracted Resume Information")


    st.write("👤 **Name:**")

    if resume_info["name"]:
        st.write(resume_info["name"])
    else:
        st.write("Not detected")


    st.write("📧 **Email:**")

    if resume_info["email"]:
        st.write(resume_info["email"])
    else:
        st.write("Not detected")


    st.write("📱 **Phone:**")

    if resume_info["phone"]:
        st.write(resume_info["phone"])
    else:
        st.write("Not detected")


    st.write("🛠️ **Detected Skills:**")

    if resume_info["skills"]:

        for skill in resume_info["skills"]:
            st.write(f"• {skill}")

    else:

        st.write("No technical skills detected.")


    st.write("🎓 **Education:**")

    if resume_info["education"]:

        for item in resume_info["education"]:
            st.write(f"• {item}")

    else:

        st.write("Not detected")


    st.write("💻 **Projects:**")

    if resume_info["projects"]:

        for item in resume_info["projects"]:
            st.write(f"• {item}")

    else:

        st.write("Not detected")


    st.write("💼 **Experience:**")

    if resume_info["experience"]:

        for item in resume_info["experience"]:
            st.write(f"• {item}")

    else:

        st.write("Not detected")


    st.write("📜 **Certifications:**")

    if resume_info["certifications"]:

        for item in resume_info["certifications"]:
            st.write(f"• {item}")

    else:

        st.write("Not detected")


    # --------------------------------------------------
    # DISPLAY JOB DESCRIPTION ANALYSIS
    # --------------------------------------------------

    st.subheader("💼 Job Description Analysis")


    st.write("🎯 **Job Role:**")

    if job_data["job_role"]:
        st.write(job_data["job_role"])
    else:
        st.write("Not detected")


    st.write("🛠️ **Required Skills:**")

    if job_data["required_skills"]:

        for skill in job_data["required_skills"]:
            st.write(f"• {skill}")

    else:

        st.write("No required skills detected.")


    st.write("🎓 **Qualifications:**")

    if job_data["qualifications"]:

        for qualification in job_data["qualifications"]:
            st.write(f"• {qualification}")

    else:

        st.write("Not detected")


    st.write("💼 **Required Experience:**")

    if job_data["experience"]:
        st.write(job_data["experience"])
    else:
        st.write("Not specified")


    # --------------------------------------------------
    # USER PROVIDED INFORMATION
    # --------------------------------------------------

    st.subheader("👤 User Provided Information")


    st.write("💼 **Job Description:**")
    st.write(career_data["job_description"])


    st.write("🛠️ **Skills Provided:**")
    st.write(career_data["skills"])


    st.write("🎯 **Career Preferences:**")
    st.write(career_data["career_preferences"])


    # --------------------------------------------------
    # SUCCESS
    # --------------------------------------------------

    st.success(
        "🎉 Resume and job description processing completed!"
    )

