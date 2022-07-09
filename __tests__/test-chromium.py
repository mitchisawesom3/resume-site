from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
  "--headless",
  "--disable-gpu",
  "--window-size=1920,1200",
  "--ignore-certificate-errors",
#  "--disable-extensions",
  "--no-sandbox",
  "--disable-dev-shm-usage",
  "--enable-javascript",
  '--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"'
]
for option in options:
  chrome_options.add_argument(option)

chrome_options.BinaryLocation = "/usr/bin/chromium-browser"
service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service,options=chrome_options)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))

#wait = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, "website-counter").get_attribute("value") >= 0)
#driver.implicitly_wait(10)
driver.get('https://www.mitchbounds.com')
driver.implicitly_wait(10)
#wait = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.CLASS_NAME, "website-counter").get_attribute("value") >= 0)
print(driver.title)
print(driver.page_source)
