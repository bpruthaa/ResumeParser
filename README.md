# ResumeParser
# 🧠 Resume Shortlisting App

An AI-powered, feature-rich resume parsing and shortlisting system built with **Streamlit**. This tool parses multiple PDF resumes, compares them against a given job description using both keyword-based and semantic AI methods, and generates a detailed shortlisting report — all in real-time!

---

## 🚀 Features

### 🔍 Resume Parsing & AI Shortlisting
- Parse multiple resumes in bulk (PDF format)
- Extract key fields: **Name, Email, Phone, LinkedIn, GitHub, Skills, Education, Experience**
- AI-driven scoring:
  - ✅ **Match Score**: based on keyword overlap
  - 🧠 **Semantic Score**: deep similarity using sentence embeddings (NLP)
- Auto-calculates **Total Experience (yrs)** even if not explicitly mentioned
- Detects **Keyword Gaps** (skills or terms missing in resume vs JD)

### 📊 Visual Dashboards
- 📅 **Career Timeline** bar chart
- 📈 **Score Distribution** histogram
- 🔎 View and filter:
  - Parsed Resumes
  - ✅ Shortlisted (above threshold)
  - ❌ Not Shortlisted

### 📁 Excel Export
- Download results as `.xlsx` with three sheets:
  - Parsed_Resumes
  - Shortlisted
  - Unlisted

---

## 📦 Directory Structure

