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
# click on cart icon
driver.find_element(By.CSS_SELECTOR, '[aria-label="cart 0 items"]').click()
sleep(5)
# verify 'Your cart is empty' message displays
driver.find_element(By.XPATH, '//h1[text()="Your cart is empty"]').text
# verification
actual_text = driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']").text
expected_text = 'Your cart is empty'
assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
print('Test case passed')