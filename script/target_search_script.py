from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
driver.find_element(By.ID, 'search').send_keys('umbrella')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(10)
# verification
#driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']")
# by checking text
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
#print('Actual text:\n', actual_text)
#assert 'tea' in actual_text, f'Error. Text tea not in {actual_text}'

expected_text = 'umbrella'
assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
print('Test case passed')