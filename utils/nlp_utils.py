import re
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return ""

def extract_emails(text):
    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    return emails[0] if emails else ""

def extract_phone_numbers(text):
    phones = re.findall(r"(\+?\d[\d\s\-]{8,}\d)", text)
    return phones[0] if phones else ""

def extract_links(text):
    linkedin = None
    github = None
    links = re.findall(r"(https?://[^\s]+|www\.[^\s]+)", text)
    for link in links:
        if "linkedin.com" in link:
            linkedin = link.strip(".,; ")
        elif "github.com" in link:
            github = link.strip(".,; ")
    return linkedin, github

def extract_skills(text, skill_keywords):
    found = []
    text_lower = text.lower()
    for skill in skill_keywords:
        if skill.lower() in text_lower:
            found.append(skill)
    return list(set(found))

def extract_languages(text):
    common_languages = ["English", "Hindi", "Spanish", "French", "German", "Mandarin", "Gujarati"]
    return [lang for lang in common_languages if lang.lower() in text.lower()]
