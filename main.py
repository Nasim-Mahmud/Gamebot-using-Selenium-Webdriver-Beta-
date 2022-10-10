from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

LINK = "https://orteil.dashnet.org/cookieclicker/"

# Removing deprecationWarning: executable_path has been deprecated
chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get(LINK)

actions = ActionChains(driver)
driver.implicitly_wait(10)
driver.find_element(By.ID, "langSelect-EN").click()
driver.implicitly_wait(50)
driver.find_element(By.XPATH, '/html/body/div[1]/div/a[1]').click()

game_on = True
for n in range(20):
    driver.find_element(By.ID, "bigCookie").click()

cookie_number = driver.find_element(By.ID, 'cookies').text.split(" ")[0]
print(int(cookie_number))
print(type(cookie_number))

# driver.quit()
