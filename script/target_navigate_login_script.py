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

# Open the url
driver.get('https://www.target.com/')
# Click Sign In
driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(2)
# When right side navigation menu opens, click sign-in
driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']").click()
sleep(2)
# Verify Sign-In form opens
driver.find_element(By.CSS_SELECTOR, "button[id='login']")
# by checking text
actual_text = driver.find_element(By.CSS_SELECTOR, "button[id='login']")
expected_text = 'Sign in with password'
assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
print('Test case passed')