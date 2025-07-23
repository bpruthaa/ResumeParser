import fitz  # PyMuPDF

def extract_resume_data(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()

    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "LinkedIn": extract_linkedin(text),
        "GitHub": extract_github(text),
        "Experience": extract_experience(text),
        "FullText": text
    }

import re

def extract_name(text):
    lines = text.strip().split('\n')
    return lines[0].strip() if lines else ""

def extract_email(text):
    match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    return match.group() if match else ""

def extract_phone(text):
    match = re.search(r"\+?\d[\d\s\-]{8,}", text)
    return match.group().strip() if match else ""

def extract_linkedin(text):
    match = re.search(r"linkedin\.com/in/\S+", text, re.IGNORECASE)
    return match.group() if match else ""

def extract_github(text):
    match = re.search(r"github\.com/\S+", text, re.IGNORECASE)
    return match.group() if match else ""

def extract_experience(text):
    matches = re.findall(r"(?P<Role>[\w\s]+)\s+(\d{4}).*?(\d{4}|present)", text, re.IGNORECASE)
    return [{"Role": m[0], "Start": m[1], "End": m[2]} for m in matches]
