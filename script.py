from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, os
from datetime import datetime

urls = {
    "arrivi_str": "https://iechub.rfi.it/ArriviPartenze/ArrivalsDepartures/Monitor?placeId=2791&arrivals=True",
    "partenze_str": "https://iechub.rfi.it/ArriviPartenze/ArrivalsDepartures/Monitor?placeId=2791&arrivals=False",
    "arrivi_chv": "https://iechub.rfi.it/ArriviPartenze/ArrivalsDepartures/Monitor?Arrivals=True&Search=chivasso&PlaceId=1105",
    "partenze_chv": "https://iechub.rfi.it/ArriviPartenze/ArrivalsDepartures/Monitor?Arrivals=False&Search=chivasso&PlaceId=1105",
    "arrivi_tpn": "https://iechub.rfi.it/ArriviPartenze/ArrivalsDepartures/Monitor?placeId=2876&arrivals=True"
}

os.makedirs("screenshots", exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--headless=new")   # nuova modalità headless
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument(f"--user-data-dir=/tmp/chrome-user-data")

driver = webdriver.Chrome(options=chrome_options)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

for name, url in urls.items():
    driver.get(url)
    time.sleep(5)
    filename = f"{name}_{timestamp}.png"
    path = os.path.join("screenshots", filename)
    driver.save_screenshot(path)
    print(f"Screenshot salvato: {path}")

driver.quit()
