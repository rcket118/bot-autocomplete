import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Install chromedriver otomatis
chromedriver_autoinstaller.install()

# Keyword list
keywords = [
    "unditoto", "daftar unditoto", "link unditoto", "prediksi hk malam ini",
    "togel terpercaya 2025", "login unditoto", "link alternatif unditoto",
    "link aman unditoto", "apakah unditoto terpercaya", "slot unditoto",
    "togel unditoto", "macau unditoto"
]

# Setup Chrome headless
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Jalankan browser
driver = webdriver.Chrome(options=chrome_options)

for keyword in keywords:
    driver.get("https://www.google.com")
    box = driver.find_element(By.NAME, "q")
    box.send_keys(keyword)
    time.sleep(1.5)
    suggestions = driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li span")
    print(f"\nKeyword: {keyword}")
    for s in suggestions:
        print(f" - {s.text}")

driver.quit()
