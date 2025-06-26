import selenium
import streamlit

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

import requests
from bs4 import BeautifulSoup 

url = ("https://www.baseball-almanac.com/yearmenu.shtml" )
response = requests.get("https://www.baseball-almanac.com/yearmenu.shtml" )
driver.get("https://www.baseball-almanac.com/yearmenu.shtml")

print(type(response))

title = driver.title ("MLB History Year-by-Year (1876-2025) | Baseball Almanac")

print(f"pag title{driver.title}")


wait = WebDriverWait(driver, 8)
table = wait.until(EC.Presence_of_element_located((By.TAG_NAME, "table")))

driver.get

import sqlite3
import pandas as pd

with sqlite3.connect( "mlb_yearly_index.avg") as conn:
        cursor = conn.cursor()
        conn.execute("PRAGMA foreign_keys = 1")
         
        try:
            df = pd.read_csv("mlb_yearly_index_cleaned.csv")
              

            cursor.execute("DROP TABLE IF EXISTS mbl_yearly_index")

        cursor.execute("""
            CREATE TABLE mlb_yearly_index( 
 
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
                    INSERT INTO mbl_year_index (year, league, player, team, avg)
                    VALUES (?,?,?,?,?)
                """, (row["Year"], row["League"], row["Player"], row["Team"], row["DB"]))
                                    
            conn.commit() 
        
        print("Loaded data into mbl_yearly_index_avg.db")
        except (sqlite3.Error, pd.errors.EmptyDataError FileNotFoundError)as e:
        print(f"Error ocurred: {e}")


               
url = "https://www.baseball-almanac.com/yearmenu.shtml"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

year_links = soup.select("ul > li > a")

data = []

for link in year_links:
        year = link.text.strip()
        href = link.get("href")
        full_url = "https://www.baseball-almanac.com/" + href if href else None
        data.append({"Year": year, "URL": full_url})
print("dataframe")

# Save to CSV
df = pd.DataFrame(data)
print("csv")
df.to_csv("mlb_yearly_index.csv", index=False)


print(df.head())




