import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

import requests
import re

DB_PATH = "../mlb_history.db"

@st.cache_data
def get_table_names():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    return sorted(tables)

@st.cache_data
def load_table(table_name):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql(f'SELECT * FROM "{table_name}"', conn)
    conn.close()
    return df

# 
st.title(" MLB History Dashboard (1876–2025)")
st.markdown("Data from [Baseball Almanac](https://www.baseball-almanac.com/yearmenu.shtml)")

# Sidebar
tables = get_table_names()
years = sorted({t.split("_")[1] for t in tables})
selected_year = st.sidebar.selectbox("Select Year", years)


year_tables = [t for t in tables if selected_year in t]

selected_table = st.sidebar.selectbox("Select Table", year_tables)

df = load_table(selected_table)

# Show DataFrame
st.subheader(f" Table: {selected_table}")
st.dataframe(df)


if "Player" in df.columns:
    player = st.text_input("Filter by Player Name")
    if player:
        df = df[df["Player"].str.contains(player, case=False, na=False)]

if "Team" in df.columns:
    team = st.selectbox("Filter by Team", ["All"] + sorted(df["Team"].dropna().unique().tolist()))
    if team != "All":
        df = df[df["Team"] == team]

# Plotting
if "HR" in df.columns and "Player" in df.columns:
    st.subheader(" Home Run Leaders")
    hr_df = df[["Player", "HR"]].dropna()
    hr_df["HR"] = pd.to_numeric(hr_df["HR"], errors="coerce")
    top_hr = hr_df.sort_values(by="HR", ascending=False).head(10)
    
    fig, ax = plt.subplots()
    ax.barh(top_hr["Player"], top_hr["HR"], color='skyblue')
    ax.invert_yaxis()
    ax.set_xlabel("Home Runs")
    st.pyplot(fig)

# Export
st.download_button("Download table as CSV", df.to_csv(index=False), file_name=f"{selected_table}.csv", mime="text/csv")

print(df.head())