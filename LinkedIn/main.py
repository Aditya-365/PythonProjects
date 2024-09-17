from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(0.5)

# ------------------------------------ CONSTANTS --------------------------------------------------- #
email = "r33347761@gmail.com"
password = "Ubk9pkV%"
# ------------------------------------ SIGN IN ------------------------------------------------------ #

driver.get("https://www.linkedin.com/checkpoint/lg/sign-in-another-account")

email_txt = driver.find_element(by=By.ID, value="username")
email_txt.send_keys(email)

password_txt = driver.find_element(by=By.ID, value="password")
password_txt.send_keys(password)

sign_in = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]')
sign_in.click()

# --------------------------------- GO TO JOBS ------------------------------------------------------ #

goto_jobs = driver.find_element(by=By.LINK_TEXT, value="Jobs")
goto_jobs.click()

# -------------------------------- CHOOSE ALL JOB ------------------------------------------------------ #

jobs_list = driver.find_elements(by=By.XPATH, value='//*[@id="jobs-home-vertical-list__entity-list"]/li[1]')
for n in range(len(jobs_list)):
    try:
        jobs_list[n].click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR,".jobs-save-button.artdeco-button.artdeco-button--3.artdeco-button--secondary").click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, "li-icon.artdeco-button__icon").click()
        time.sleep(5)
    except NoSuchElementException:
        continue

driver.quit()