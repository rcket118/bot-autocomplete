from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

keywords = [
    "unditoto", "login unditoto", "togel unditoto",
    "prediksi hk malam ini", "slot unditoto", "link alternatif unditoto"
]

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

for keyword in keywords:
    driver.get("https://www.google.com")
    box = driver.find_element(By.NAME, "q")
    box.send_keys(keyword)
    time.sleep(2)
    results = driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li span")
    print(f"\nKeyword: {keyword}")
    for res in results:
        print(f" - {res.text}")

driver.quit()
