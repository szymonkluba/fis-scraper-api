import os
from time import sleep

import environ
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.conf import settings

environ.Env.read_env(os.path.join(settings.BASE_DIR, ".env"))


def get_dynamic_content(url):
    GOOGLE_CHROME_PATH = os.environ.get("GOOGLE_CHROME_BIN")
    CHROMEDRIVER_PATH = os.environ.get("CHROMEDRIVER_PATH")

    chrome_options = Options()
    chrome_options.binary_location = GOOGLE_CHROME_PATH
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(get_proxy_url())

    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
    driver.get(url)
    sleep(2)
    return driver.page_source


def get_proxy_url():
    response = requests.get("http://proxy11.com/api/proxy.json?key=NTI5NQ.Y2WHTw.Uc9KF2jC5-3XlCa31jwDmyegEYE&limit=1").json()[0]

    return f"--proxy-server={response['ip']}:{response['port']}"
