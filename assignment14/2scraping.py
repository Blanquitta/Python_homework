

import os
import requests
import pandas as pd
import sqlite3
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from sqlalchemy import create_engine
from sqlalchemy.types import Integer, DateTime, Float, Text 

from bs4 import BeautifulSoup 

DATA_DIR = 'csv_files'

import sqlite3

csv_file =( "../mlb_history.db")

#where we the infomtioSSn from

with sqlite3.connect( "../mlb_history.db") as conn:
 

    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS mlb_history_avg.db")
    conn.execute("PRAGMA foreign_keys = 1")

try:
    df = pd.read_csv("mlb_history_db_cleaned.csv")

    with sqlite3.connect( "../mlb_history.db") as conn:
              cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE mlb_history_db( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            year INTEGER,
            league TEXT,
            player TEXT,
            team TEXT,
            avg REAL
        )
    """ )

    for _,row in df.iterrows():
               cursor.execute("""
                    INSERT INTO mbl_history__avg_db (year, league, player, team, db)
                    VALUES (?,?,?,?,?)
                """, (row["Year"], row["League"], row["Player"], row["Team"], row["DB"]))
                                    
    conn.commit() 
            
    print("Loaded data into mbl_history_db")

except (sqlite3.Error, pd.errors.EmptyDataError, FileNotFoundError)as e:
    print(f"Error ocurred: {e}")

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    print(cursor.fetchall())  

    with sqlite3.connect( "../mlb_history.db") as conn:


        driver.get("https://www.baseball-almanac.com/players/player.php?p=rodrial01")

title = driver.title


# Constants
BASE_URL = "https://www.baseball-almanac.com/"
YEAR_INDEX_URL = BASE_URL + "yearmenu.shtml"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# create folders
os.makedirs("season_csvs", exist_ok=True)

#  all year URLs
response = requests.get(YEAR_INDEX_URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")
links = soup.select("ul > li > a")

year_url_pairs = []

for link in links:
    year_text = link.text.strip()
    href = link.get("href")
    if href and href.startswith("yearly/yr") and href.endswith("a.shtml"):
        full_url = BASE_URL + href
        year_url_pairs.append((year_text, full_url))


for year, url in year_url_pairs:
    try:
        tables = pd.read_html(url)  # Get all tables
        for idx, table in enumerate(tables):
            filename = f"season_csvs/season_{year}_table{idx}.csv"
            table.to_csv(filename, index=False)
            print(f"Saved: {filename}")
    except Exception as e:
        print(f"Failed for {year}: {e}")



print(os.listdir("season_csvs"))
conn = sqlite3.connect("../mlb_history.db")
try:
    df = pd.read_csv("season_csvs/season_2023_table0.csv")  
    df.to_sql("mlb_history", conn, if_exists="replace", index=False)
    print("Successfully imported to 'mlb_history' table.")
except Exception as e:
    print(f"Error importing to mlb_history: {e}")
conn.close()

DATA_DIR = '../mlb_history.db'  # Folder where CSVs are stored


engine = create_engine(f'sqlite:///{DB_FILE}')

table_name = os.path.splitext(os.path.basename(csv_file))[0]


