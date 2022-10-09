from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

LINK = "https://orteil.dashnet.org/cookieclicker/"

# Removing deprecationWarning: executable_path has been deprecated
chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get(LINK)

terms = driver.find_element(By.CLASS_NAME, 'cc_container--open cc_btn cc_btn_accept_all')
terms.click()
lang = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
lang.click()
# cookie = driver.find_element(By.ID, "bigCookie")
# cookie.click()


# driver.quit()

