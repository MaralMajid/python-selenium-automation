from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# for Amazon Logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# for email field
driver.find_element(By.ID,"ap_email")

# for Continue button
driver.find_element(By.XPATH, "//input[@class='a-button-input']")

# for Conditions of use link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Conditions of Use']")


# for Privacy Notice link
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")


# for Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")


# for Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')


# for Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")

# for Create your Amazon account button
driver.find_element(By.XPATH, "//span[@class='a-button-inner']//a[@id='createAccountSubmit']")
