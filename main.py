from selenium import webdriver

chrome_drive_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

driver.get("https://www.amazon.com")