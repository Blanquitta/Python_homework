import selenium
import streamlit

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
import pandas as pd
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

from bs4 import BeautifulSoup 

url = ("https://www.baseball-almanac.com/yearmenu.shtml" )
driver.get("https://www.baseball-almanac.com/yearmenu.shtml")

title = driver.title 

print(f"pag title{driver.title}")

import requests

import pandas as pd

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

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("mlb_yearly_index.csv", index=False)

print(df.head())


