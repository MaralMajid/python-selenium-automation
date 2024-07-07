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
driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26gad_source%3D1%26hvadid%3D675149237887%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9030078%26hvnetw%3Dg%26hvpone%3D%26hvpos%3D%26hvptwo%3D%26hvqmt%3De%26hvrand%3D4533709676127030797%26hvtargid%3Dkwd-10573980%26hydadcr%3D28883_14649097%26ref%3Dpd_sl_7j18redljs_e%26tag%3Damazusnavi-20%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# for Amazon logo
driver.find_element(By.CSS_SELECTOR, "[aria-label='Amazon']")

# for Create account logo
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# for your name
driver.find_element(By.CSS_SELECTOR, "input[placeholder='First and last name']")

# for mobile number or email
driver.find_element(By.CSS_SELECTOR, "input#ap_email")

# for password
driver.find_element(By.CSS_SELECTOR, "#ap_password")

# for alert message
driver.find_element(By.CSS_SELECTOR, "div[class*='a-box a-alert-inline a-alert-inline-info auth-inlined-information-message a-spacing-top-mini']")

# for Continue button
driver.find_element(By.CSS_SELECTOR, "input#continue")

# for privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

# for condition of use
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_condition_of_use']")

# for sign in
driver.find_element(By.CSS_SELECTOR, "a[class='a-link-emphasis']")