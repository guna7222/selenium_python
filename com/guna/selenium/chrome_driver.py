from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:/Users/Cyntexia/Downloads/chromedriver_win32.exe")  # chrome driver
driver = webdriver.Chrome(service=service_obj)
driver.get("http://w3schools.com")
# to get title of the web site then we can use title property
print(driver.title)
# to check whether we are directed to correct url or not
print(driver.current_url)
driver.close()
