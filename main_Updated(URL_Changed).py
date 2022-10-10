from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

LINK = "https://orteil.dashnet.org/cookieclicker/"

chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get(LINK)

