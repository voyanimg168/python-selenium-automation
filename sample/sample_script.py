from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(4) #checks for element every 100 ms & applies to all environment fxns
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10) #usually longer 10-15s vs implicit wait is 4s

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('car')

#sleep(10)
driver.wait.until(EC.element_to_be_clickable ((By.NAME, 'btnK')), message='Search btn not clickable').click()
##EC=combines top sleep & below click button lines

# click search button
#driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert 'car'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')
driver.quit()
