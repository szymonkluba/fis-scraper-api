import os
import re
import subprocess
from time import sleep

import environ
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from django.conf import settings
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

environ.Env.read_env(os.path.join(settings.BASE_DIR, ".env"))


def get_dynamic_content(url):
    try:
        process = subprocess.Popen(["chromium-browser", "-version"], stdout=subprocess.PIPE)
    except FileNotFoundError:
        process = subprocess.Popen(["google-chrome", "-version"], stdout=subprocess.PIPE)
    output = process.communicate()[0]

    version_regex = re.compile(r"[0-9.]+", re.MULTILINE)
    version = re.findall(version_regex, output.decode('utf8').strip())[0]

    driver_service = Service(ChromeDriverManager(version=version).install())

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
