import streamlit as st
import altair as alt
import pandas as pd

def experience_timeline(df):
    st.subheader("📅 Career Timeline")

    if "Experience" not in df.columns or df["Experience"].isnull().all():
        st.info("No valid experience data to generate timeline.")
        return

    timeline_data = []

    for _, row in df.iterrows():
        name = row.get("Name", "Unknown")
        experiences = row.get("Experience", [])

        # Experience must be a list of dicts like [{"Role": "Data Scientist", "Start": "2019", "End": "2022"}]
        if isinstance(experiences, list):
            for exp in experiences:
                try:
                    timeline_data.append({
                        "Name": name,
                        "Role": exp.get("Role", "Unknown"),
                        "Start": pd.to_datetime(str(exp.get("Start", "1900")), errors='coerce'),
                        "End": pd.to_datetime(str(exp.get("End", "1900")), errors='coerce')
                    })
                except Exception as e:
                    continue

    if not timeline_data:
        st.warning("No valid experience entries parsed for timeline.")
        return

    chart_df = pd.DataFrame(timeline_data)
    chart_df.dropna(subset=["Start", "End"], inplace=True)

    chart = alt.Chart(chart_df).mark_bar().encode(
        x='Start:T',
        x2='End:T',
        y=alt.Y('Name:N', sort='-x'),
        color='Role:N',
        tooltip=['Role', 'Start', 'End']
    ).properties(
        title="Career Timeline",
        width=700,
        height=400
    )

    st.altair_chart(chart, use_container_width=True)

def score_distribution_chart(df):
    st.subheader("📊 Score Distribution")

    if "Match Score (%)" not in df.columns:
        st.warning("Match Score (%) column missing.")
        return

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Match Score (%):Q", bin=alt.Bin(maxbins=20)),
        y='count():Q',
        tooltip=['count():Q']
    ).properties(
        width=700,
        height=300
    )

    st.altair_chart(chart, use_container_width=True)
