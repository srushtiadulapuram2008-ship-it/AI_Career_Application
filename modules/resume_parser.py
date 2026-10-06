from pypdf import PdfReader


def extract_pdf_text(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text
    from docx import Document


def extract_docx_text(file):

    document = Document(file)

    text = ""

    for paragraph in document.paragraphs:

        if paragraph.text.strip():
            text += paragraph.text + "\n"

    return text
def extract_resume_text(file):

    filename = file.name.lower()

    if filename.endswith(".pdf"):

        text = extract_pdf_text(file)

    elif filename.endswith(".docx"):

        text = extract_docx_text(file)

    else:

        raise ValueError(
            "Unsupported file format. Please upload PDF or DOCX."
        )

    return text
def clean_resume_text(text):

    lines = text.splitlines()

    cleaned_lines = []

    for line in lines:

        line = line.strip()

        if line:
            cleaned_lines.append(line)

    return "\n".join(cleaned_lines)