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
#driver.get('https://www.amazon.com/')
#Amazon Logo
#driver.find_element("//a[@class='nav-logo-link nav-progressive-attribute']")
##Email Field
#driver.find_element("//input[@type='email' and @id='ap_email']")
##Continue Button
#driver.find_element("//input[@type='submit' and @id='continue']")
##Conditions of Use link
#driver.find_element("//*[@id='legalTextRow']/a[1]")
##Privacy Notice Link
#driver.find_element("//*[@id='legalTextRow']/a[2]")
##Need Help Link
#driver.find_element("//span[@class='a-expander-prompt']")
##Forgot Your Password Link
#driver.find_element("//a[@id='auth-fpp-link-bottom']")
##Other Issues With Sign-In Link
#driver.find_element("//a[@id='ap-other-signin-issues-link']")
##Create Your Amazon Account Button
#driver.find_element("//a[@id='createAccountSubmit']")

###

#Create Test Case for Sign-In Page
driver.get('https://www.target.com/')
#Click top right sign-in icon)
driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 cOUViz h-margin-r-x3']").click()
sleep(2)
#Open Side Navigation (Sign-In Button)
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
sleep(2)
#driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
#Go to login page
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
#Validate successful login
print('Test Case Passed')


###

##Create Test Case to Search for Product on Target
# open the url
driver.get('https://www.target.com/')
driver.find_element(By.ID, 'search').send_keys('umbrella')
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(5)
# verification
driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']")
# by checking text
actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
expected_text = 'umbrella'
assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'
print('test case passed')
driver.quit()