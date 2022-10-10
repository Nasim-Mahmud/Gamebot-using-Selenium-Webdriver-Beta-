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
cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
cursor_price = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" ")[2]
cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')


for n in range(20):
    cookie_number = driver.find_element(By.ID, "money").text
    if int(cookie_number) > int(cursor_price):
        cursor.click()
    cookie.click()

print(driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" "))
driver.quit()
