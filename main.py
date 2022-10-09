from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

LINK = "https://www.python.org/"

# Removing deprecationWarning: executable_path has been deprecated
chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get(LINK)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_dates[n].text
    }

print(events)


driver.quit()

