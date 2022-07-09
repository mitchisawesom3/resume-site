#!/usr/bin/python3.9
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
chrome_options = Options()
options = [
  "--headless",
  "--disable-gpu",
  "--window-size=1920,1200",
  "--ignore-certificate-errors",
  "--disable-extensions",
  "--no-sandbox",
  "--disable-dev-shm-usage",
  "--enable-javascript",
  '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"'
]
for option in options:
  chrome_options.add_argument(option)
#chrome_options.add_argument('--disable-blink-features=AutomationControlled')
firefox_options = FirefoxOptions()
firefox_options.add_argument('--headless')
def test_site():
# driver_path = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
  chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
  browser = webdriver.Chrome(service=chrome_service, options=chrome_options)
#  wait = WebDriverWait(browser, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, "website-counter").get_attribute("value") >= 0)
  browser.implicitly_wait(10)
  browser.get("https://www.mitchbounds.com")
#  wait = WebDriverWait(browser, timeout=5).until(lambda d: d.find_element(By.CLASS_NAME, "website-counter").get_attribute("value") >= 0)
  print(browser.find_element(By.CLASS_NAME, "website-counter").get_attribute("outerHTML"))
  print(browser.page_source)
  browser.quit()

  browser = webdriver.Firefox(options=firefox_options)
if __name__ == "__main__":
  test_site()
  print("Everything passed") 
