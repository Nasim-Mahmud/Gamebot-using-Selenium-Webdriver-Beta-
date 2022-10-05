from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_drive_path = "C:\Development\chromedriver.exe"
service_obj = Service(executable_path=chrome_drive_path)
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.amazon.com")
# driver.close()
