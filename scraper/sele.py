import os
import re
import subprocess
from time import sleep

import environ
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

environ.Env.read_env(os.path.join(settings.BASE_DIR, ".env"))


def get_dynamic_content(url):
    try:
        process = subprocess.Popen(
            ["chromium-browser", "-version"], stdout=subprocess.PIPE
        )
    except FileNotFoundError:
        process = subprocess.Popen(
            ["google-chrome", "-version"], stdout=subprocess.PIPE
        )
    output = process.communicate()[0]

    version_regex = re.compile(r"\d{2,3}\.\d{1,2}", re.MULTILINE)
    version = re.findall(version_regex, output.decode("utf8").strip())[0]

    try:
        print(f"Chromedriver version: {version}")
        driver_service = Service(ChromeDriverManager(version=version).install())
    except ValueError as error:
        print(error)
        driver_service = Service(executable_path=os.environ.get("CHROMEDRIVER_PATH"))

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
