from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# Removing deprecationWarning: executable_path has been deprecated
chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get("https://selenium-python.readthedocs.io/")

# Comment: Class a-offscreen not working!
price1 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[1]/h3").text
print(price1)
# price2 = driver.find_element(By.CLASS_NAME, "a-price-fraction").text
# print(price2)
#
driver.quit()
# price = price1 + "." + price2
# print(price)
