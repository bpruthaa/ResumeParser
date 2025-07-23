import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime

def show_timeline(df):
    st.subheader("📅 Career Timeline")

    timeline_data = []
    current_year = datetime.now().year

    for _, row in df.iterrows():
        name = row.get("Name", "Unknown")
        experience_list = row.get("Experience", [])

        if isinstance(experience_list, list):
            for exp in experience_list:
                role = exp.get("Role", "Unknown")
                start = exp.get("Start", "")
                end = exp.get("End", "")

                try:
                    start_year = int(start)
                except (ValueError, TypeError):
                    start_year = None

                try:
                    if str(end).lower() in ["present", "current", "ongoing"]:
                        end_year = current_year
                    else:
                        end_year = int(end)
                except (ValueError, TypeError):
                    end_year = current_year

                if start_year:
                    timeline_data.append({
                        "Name": name,
                        "Role": role,
                        "Start": start_year,
                        "End": end_year
                    })

    if not timeline_data:
        st.info("⚠️ No timeline data available to display.")
        return

    chart_df = pd.DataFrame(timeline_data)

    chart = alt.Chart(chart_df).mark_bar().encode(
        x='Start:O',
        x2='End:O',
        y=alt.Y('Name:N', sort='-x'),
        color='Role:N',
        tooltip=['Role', 'Start', 'End']
    ).properties(width=750, height=400)

    st.altair_chart(chart, use_container_width=True)
