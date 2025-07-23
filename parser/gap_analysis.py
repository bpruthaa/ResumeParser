def find_keyword_gaps(text, keywords):
    text_words = text.lower()
    missing = [kw for kw in keywords if kw not in text_words]
    return ", ".join(missing)
