from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

LINK = "http://orteil.dashnet.org/experiments/cookie/"

chrome_drive_path = "C:\Development\chromedriver.exe"
s = Service(chrome_drive_path)
driver = webdriver.Chrome(service=s)
driver.get(LINK)


# driver.implicitly_wait(50)
# Cursor price
def cursor_price():
    cp = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" ")[2]
    return int(cp)


# Grandma price
def grandma_price():
    gp = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" ")[2]
    return int(gp)


# Factory price
def factory_price():
    fp = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" ")[2]
    return int(fp)


# Mine price
def mine_price():
    mp = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" ")[2]
    return int(mp)


# Shipment price
def shipment_price():
    sp = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" ")[2]
    return int(sp)


# Alchemy price
def alchemy_price():
    ap = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" ")[2]
    return int(ap)


# Portal price
def portal_price():
    pp = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" ")[2]
    return int(pp)


# Time Machine price
def time_machine_price():
    tmp = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split(" ")[2]
    return int(tmp)


driver.quit()
