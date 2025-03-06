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
driver.get('https://www.amazon.com/')
# By ID
driver.find_element(By.ID, 'twotabsearchtextbox') #search text box
driver.find_element(By.ID, 'nav-search-submit-button') #magnify glass
# By XPath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH,"//input[@role='searchbox']")
# By XPath, multiple attributes (shorter, the better)
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords']")
# By XPATH, any tag
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']") #[* = wild card/all tag]
# By XPATH, using text (function, not attribute)
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
driver.find_element(By.XPATH, "//h2[text()='Luxury bestsellers']")
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and text()='Best Sellers']")
driver.find_element(By.XPATH, "//h2[contains(text(), 'Luxury bestsellers')]")
# Partial Text Match (only works if run automation in one language, not in multiple languages)
driver.find_element(By.XPATH, "//h2[contains(text(), 'Luxury')]")
# Partial Attribute Match
driver.find_element(By.XPATH, "//select[@aria-describedby='searchDropdownDescription']")
driver.find_element(By.XPATH, "//select[contains(@class, 'nav-search-dropdown')]")


