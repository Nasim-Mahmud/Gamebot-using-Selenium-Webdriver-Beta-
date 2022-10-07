from selenium import webdriver

chrome_drive_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_drive_path)

driver.get("https://www.amazon.com/FIODIO-Comfortable-"
           "Anti-Ghosting-Resistant-Multimedia/dp/B086168Y25/ref=sr_1_1_"
           "sspa?keywords=gaming+keyboard&pd_rd_r=5d5b7d6a-866c-4071-b353-c9c2e00ef674&pd_"
           "rd_w=Cpi3v&pd_rd_wg=YqINu&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=F5"
           "4CV71S6YMFKCMAKY66&qid=1665017179&qu=eyJxc2MiOiI3LjE0IiwicXNhIjoiNi44MCIsInFzcCI6IjYu"
           "MjEifQ%3D%3D&sr=8-1-spons&psc=1")
price = driver.switch_to.__class__
print(price.text)




driver.quit()