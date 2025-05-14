#6

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os
import time

# Set up headless Chrome
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load OWASP Top 10 page
url = "https://owasp.org/www-project-top-ten/"
driver.get(url)

time.sleep(3)  # Wait for the page to load

# XPath to find top 10 vulnerability titles and links
# This XPath might change depending on OWASP's layout
items = driver.find_elements(By.XPATH, '//div[contains(@class,"project-top-ten")]/ul/li/a')

# Extract title and link for each vulnerability
top_10 = []
for item in items[:10]:  # Get only top 10
    title = item.text.strip()
    href = item.get_attribute("href")
    top_10.append({"Title": title, "Link": href})

# Print list to verify
print(top_10)

# Save to CSV
output_folder = "python_homework/assignment9"
os.makedirs(output_folder, exist_ok=True)

csv_path = os.path.join(output_folder, "owasp_top_10.csv")
df = pd.DataFrame(top_10)
df.to_csv(csv_path, index=False)

driver.quit()