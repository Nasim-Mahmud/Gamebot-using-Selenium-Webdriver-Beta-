from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

LINK = "http://orteil.dashnet.org/experiments/cookie/"

chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get(LINK)

driver.implicitly_wait(50)
driver.find_element(By.XPATH, '//*[@id="whole"]/div[1]/div/a[1]').click()

game_on = True
while game_on:
    cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
    cookie.click()
