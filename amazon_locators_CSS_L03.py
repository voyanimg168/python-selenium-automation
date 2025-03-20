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
driver.('https://www.amazon.com/')
#Logo on Create Amazon Account Page
driver.find_element(By.CSS_SELECTOR, ".a-icon-logo")
#Find text 'Create Account'
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
#Find entry box 'Your Name'
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
#Find entry box 'Email'
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
#Find entry box 'Password'
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
#Find 'Password must be at least 6 characters'
driver.find_element(By.CSS_SELECTOR, "[id='ap_password_context_message_section'git]")
#Find entry box 'Re-enter Password'
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
#Find button 'Create your Amazon account'  or 'Continue'
driver.find_element(By.CSS_SELECTOR, "input#continue.a-button-input")
#Find link 'Conditions of Use'
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_condition_of_use']")
#Find link 'Privacy Notice'
driver.find_element(By.CSS_SELECTOR, "[href*='ap_register_notification_privacy_notice']")
#Find link 'Sign in'
driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")

