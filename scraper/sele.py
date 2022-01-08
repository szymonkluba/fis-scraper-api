import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_dynamic_content(url):
    GOOGLE_CHROME_PATH = os.environ.get("$GOOGLE_CHROME_BIN")
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    chrome_options = Options()
    chrome_options.binary_location = GOOGLE_CHROME_PATH
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    driver.get(url)
    sleep(2)
    return driver.page_source
