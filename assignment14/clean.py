
import pandas as pd
import streamlit as st
url = "https://www.baseball-almanac.com/yearmenu.shtml"

original_df = pd.read_csv("baseball-almanac.csv")
df = pd.read_csv("../data/homerun_avg_cleaned.csv")
# Load CSV
df = pd.read_csv("homerun_avg_cleaned.csv")
st.write(" Raw Data:", df.head())
year_url = "https://www.baseball-almanac.com/yearly/yr1995a.shtml"
tables = pd.read_html(year_url)


#  rows with nulls in important columns
df = df.dropna(subset=["Player", "Year", "HR", "Games"])
 
removed_rows.to.csv("removed.text",index=False, sep="\t")
# data types
df = cleaned_rows.copy()

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["HR"] = pd.to_numeric(df["HR"], errors="coerce")
df["Games"] = pd.to_numeric(df["Games"], errors="coerce")

#  new column: HR per Game
df["HR_per_Game"] = df["HR"] / df["Games"]


df = df[(df["Year"] >= 1996) & (df["Year"] <= 2012)]


df = df.rename(columns={"HR": "HomeRuns", "Games": "GamesPlayed"})

#  cleaned data
st.write(" Cleaned & Transformed Data:", df.head())

uploaded_file = st.file_uploader("Upload homerun_avg_cleaned.csv", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(" File loaded:", df.head())
else:
    st.warning(" Please upload a CSV file to continue.")
