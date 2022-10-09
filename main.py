from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

LINK = "https://orteil.dashnet.org/cookieclicker/"

# Removing deprecationWarning: executable_path has been deprecated
chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get(LINK)


actions = ActionChains(driver)
driver.implicitly_wait(10)
language = driver.find_element(By.ID, "langSelect-EN").click()
driver.implicitly_wait(50)
terms = driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]').click()


for n in range(11):
    cookie = driver.find_element(By.ID, "bigCookie").click()

cookie_number = driver.find_element(By.ID, 'cookies').text.split(" ")
print(cookie_number[0])
print(type(cookie_number[0]))



# driver.quit()

