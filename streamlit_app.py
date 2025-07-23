import streamlit as st
import pandas as pd
import altair as alt
import re
from io import BytesIO
import fitz  # PyMuPDF

# Local modules
from parser.extractor import extract_resume_data
from parser.scorer import calculate_match_score, estimate_experience_years
from parser.gap_analysis import find_keyword_gaps
from parser.semantic import semantic_similarity_score
from visualizer.timeline import show_timeline
from visualizer.charts import experience_timeline, score_distribution_chart

# App Config
st.set_page_config(page_title="🧠 Resume Shortlisting App", layout="wide")
st.title("🧠 Resume Shortlisting App")

# Sidebar Uploads
st.sidebar.header("🔍 Upload Resumes & JD")
uploaded_files = st.sidebar.file_uploader("Upload Resume PDFs", type=["pdf"], accept_multiple_files=True)
jd_text = st.sidebar.text_area("📄 Paste Job Description", height=200)
threshold = st.sidebar.slider("✅ Shortlisting Threshold (%)", 0, 100, 60)

# Preview JD
with st.sidebar.expander("📑 Job Description Preview"):
    st.markdown(jd_text or "*No JD entered.*")

# Excel Writer
@st.cache_data
def convert_df_to_excel(Parsed_Resumes, Shortlisted, Unlisted):
    with BytesIO() as output:
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            Parsed_Resumes.to_excel(writer, sheet_name='Parsed_Resumes', index=False)
            Shortlisted.to_excel(writer, sheet_name='Shortlisted', index=False)
            Unlisted.to_excel(writer, sheet_name='Unlisted', index=False)
        return output.getvalue()

# Main Logic
if uploaded_files and jd_text:
    jd_keywords = re.findall(r'\w+', jd_text.lower())
    all_data = []

    for file in uploaded_files:
        if file is None or file.size == 0:
            st.warning(f"⚠️ Skipped empty or invalid file: {file.name}")
            continue
        try:
            data = extract_resume_data(file)
            data["Match Score (%)"] = calculate_match_score(data["FullText"], jd_keywords)
            data["Semantic Score (%)"] = semantic_similarity_score(data["FullText"], jd_text)
            data["Total Experience (yrs)"] = estimate_experience_years(data.get("Experience", ""))
            data["Keyword Gaps"] = find_keyword_gaps(data["FullText"], jd_keywords)
            all_data.append(data)
        except Exception as e:
            st.error(f"❌ Failed to process `{file.name}`: {str(e)}")

    if not all_data:
        st.warning("⚠️ No valid resumes were processed.")
    else:
        df_all = pd.DataFrame(all_data)
        df_all["Match Score (%)"] = df_all["Match Score (%)"].round(2)
        df_all["Semantic Score (%)"] = df_all["Semantic Score (%)"].round(2)
        df_all["Total Experience (yrs)"] = df_all["Total Experience (yrs)"].round(2)

        df_shortlisted = df_all[df_all["Match Score (%)"] >= threshold]
        df_unlisted = df_all[df_all["Match Score (%)"] < threshold]

        # Display Results
        st.subheader("📄 Parsed Resumes")
        st.dataframe(df_all, use_container_width=True)

        st.subheader("✅ Shortlisted Candidates")
        st.dataframe(df_shortlisted, use_container_width=True)

        st.subheader("❌ Not Shortlisted")
        st.dataframe(df_unlisted, use_container_width=True)

        # Keyword Gaps
        if "Keyword Gaps" in df_all.columns:
            with st.expander("📌 Keyword Gap Suggestions"):
                st.dataframe(df_all[["Name", "Keyword Gaps"]])

        # Charts
        with st.expander("📊 Charts & Visual Insights"):
            if "Name" in df_all.columns:
                experience_timeline(df_all)
            score_distribution_chart(df_all)

        # Timeline
        if "Name" in df_all.columns:
            show_timeline(df_all)

        # Excel Download
        excel_data = convert_df_to_excel(df_all, df_shortlisted, df_unlisted)
        st.download_button(
            label="📥 Download Excel Report",
            data=excel_data,
            file_name="resume_shortlist_results.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
else:
    st.info("📂 Upload resumes and enter a job description to begin.")
