import re

def extract_section(text, keywords):
    pattern = r"(?i)(" + keywords + r")\s*[:\-]?\s*(.*?)(\n\s*\n|$)"
    matches = re.findall(pattern, text, re.DOTALL)
    sections = [m[1].strip() for m in matches]
    return " ".join(sections).strip()

def split_experience_text(experience_section):
    # Splits multi-role experience into chunks
    chunks = re.split(r"\n(?=\s*[A-Z].*?\d{4})", experience_section)
    return [chunk.strip() for chunk in chunks if chunk.strip()]

def clean_text(text):
    text = re.sub(r"\s{2,}", " ", text)
    text = re.sub(r"[^\x00-\x7F]+", " ", text)  # Remove non-ASCII
    return text.strip()
