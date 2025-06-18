

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

with sqlite3.connect( "../mlb_history.db") as conn:
 cursor = conn.cursor()



cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())  

with sqlite3.connect( "../mlb_history.db") as conn:
 cursor = conn.cursor()

driver.get("https://www.baseball-almanac.com/players/player.php?p=rodrial01")

title = driver.title


# Constants
BASE_URL = "https://www.baseball-almanac.com/"
YEAR_INDEX_URL = BASE_URL + "yearmenu.shtml"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Create folders
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

# Import to SQLite
conn = sqlite3.connect("../mlb_history.db")

for file in os.listdir("season_csvs"):
    if file.endswith(".csv"):
        table_name = file.replace(".csv", "").replace("-", "_").replace(" ", "_")
        df = pd.read_csv(os.path.join("season_csvs", file))
        try:
            df.to_sql(table_name, conn, if_exists="replace", index=False)
            print(f"Imported to DB: {table_name}")
        except Exception as e:
            print(f"DB import failed for {table_name}: {e}")

conn.close()
print("All CSVs imported into mlb_history.db.")



DATA_DIR = '../mlb_history.db'  # Folder where CSVs are stored
DB_FILE = 'imported_data.db'  # SQLite DB file

engine = create_engine(f'sqlite:///{DB_FILE}')


def import_csv_to_db(csv_file):
    table_name = os.path.splitext(os.path.basename(csv_file))[0]

    df = pd.read_csv(csv_file)
import_csv_to_db(os.path.join("csv_directory, csv_file"))

