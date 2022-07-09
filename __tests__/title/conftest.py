import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(request):
  chrome_options = Options()
  options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
  ]
  for option in options:
    chrome_options.add_argument(option)

  service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
  request.cls.driver = webdriver.Chrome(service=service,options=chrome_options)

  yield request.cls.driver
  request.cls.driver.close()
