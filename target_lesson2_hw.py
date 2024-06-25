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
driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//span[@class='sc-58ad44c0-3 kwbrXj h-margin-r-x3']").click()
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[@class='sc-859e7637-0 hHZPQy']").click()
sleep(6)
expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH,"//span[text()='Sign into your Target account']").text
assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

print('Test passed')
driver.quit()