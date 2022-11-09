import os
from time import sleep

import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.conf import settings
from selenium.webdriver.chrome.service import Service

environ.Env.read_env(os.path.join(settings.BASE_DIR, ".env"))


def get_dynamic_content(url):
    chromedriver_path = os.environ.get("CHROMEDRIVER_PATH")

    driver_service = Service(chromedriver_path)

    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--remote-debugging-port=9222")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    driver.get(url)
    sleep(2)
    content = driver.page_source
    driver.close()

    return content
