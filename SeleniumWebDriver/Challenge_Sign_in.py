from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(0.5)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(by=By.NAME, value="fName")
fname.send_keys("Aditya")

lname = driver.find_element(by=By.NAME, value="lName")
lname.send_keys("Cherukuri")

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("chaditya972@gmail.com")

button = driver.find_element(by=By.CSS_SELECTOR, value="form button")
button.click()