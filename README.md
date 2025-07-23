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

## 💡 How It Works

1. Upload 1–10 PDF resumes
2. Paste the job description (JD) in the sidebar
3. Set your shortlisting threshold (e.g. 60%)
4. View parsed data, visual insights, and download results

---

## 📥 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/resume-shortlisting-app.git
cd resume-shortlisting-app

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

