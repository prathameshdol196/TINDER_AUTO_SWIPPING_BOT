
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

FACEBOOK_LOGIN_ID = "FACEBOOK LOGIN ID"
FACEBOOK_PASSWORD = "FACEBOOK PASSWORD"


chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://tinder.com/")
time.sleep(2)  # sleep until the data is loaded

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q-612340313"]/div/div[2]/div/div/div[1]/div[2]/button/span'))).click()
# ^ click decline cookies
time.sleep(1)  # sleep until the data is loaded

log_in = driver.find_element(By.LINK_TEXT, "Log in")  # clicks on login button
log_in.click()
time.sleep(2)  # sleep until the data is loaded

# sometimes tinder directly dont show login with facebook button but it shows more options so here we need below code
try:
    log_in_with_facebook = driver.find_element(By.XPATH, '//*[@id="q1954245907"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
    log_in_with_facebook.click()
    # ^ clicks on login with facebook button

except NoSuchElementException:
    more_options = driver.find_element(By.XPATH, '//*[@id="q1954245907"]/div/div/div[1]/div/div[3]/span/button')
    more_options.click()
    # if login with facebook button was not shown then it clicks more options
    time.sleep(1)  # sleep until the data is loaded
    log_in_with_facebook = driver.find_element(By.XPATH, '//*[@id="q1954245907"]/div/div/div[1]/div/div[3]/span/div[2]/button/span[2]')
    log_in_with_facebook.click()
    # after clicking more options login with facebook button appears then it clicks it
    time.sleep(1)  # sleep until the data is loaded

time.sleep(3)  # sleep until the data is loaded

base_window = driver.window_handles[0]  # base window
fb_login_window = driver.window_handles[1]  # popped up fb login window

driver.switch_to.window(fb_login_window)  # switched to fb login window
print(driver.title)

facebook_login_id = driver.find_element(By.NAME, "email")  # got element login field
facebook_login_id.send_keys(FACEBOOK_LOGIN_ID)  # enter login id in field

facebook_password = driver.find_element(By.NAME, "pass")  # got the password field
facebook_password.send_keys(FACEBOOK_PASSWORD)  # enter password in field
facebook_password.send_keys(Keys.ENTER)  # hitting enter
time.sleep(2)  # sleep until the data is loaded

driver.switch_to.window(base_window)  # switched back to base window
print(driver.title)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q1954245907"]/div/div/div/div/div[3]/button[1]/span'))).click()
# ^ allow location button
time.sleep(1)  # sleep until the data is loaded
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q1954245907"]/div/div/div/div/div[3]/button[2]/span'))).click()
# ^ click not intrested in notification
time.sleep(1)  # sleep until the data is loaded

time.sleep(5)
for d in range(100):
    try:
        time.sleep(2)  # 2 second delay between likes
        body = driver.find_element(By.CSS_SELECTOR, 'body')
        body.send_keys(Keys.RIGHT)
        # ^ press right arrow to like

    except NoSuchElementException:
        time.sleep(2)

    except ElementClickInterceptedException:
        time.sleep(2)
        no_thanks = driver.find_element(By.XPATH, '//*[@id="q1954245907"]/div/div/div[3]/button[2]/span')
        no_thanks.click()
