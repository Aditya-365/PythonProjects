from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path = "/Adi/UdemyPython/chromedriver.exe"
driver = webdriver.Chrome(chrome_options)

driver.get("https://www.amazon.com/Ultimate-Card-Bundle-Compatible-Pokemon/dp/B09Y8WDD2D/ref=sr_1_4_sspa?crid=23HOHRMGCDPAM&keywords=pokemon+cards&qid=1689266403&sprefix=pokemon+cards%2Caps%2C135&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")

# amazon_title = driver.title
# driver.find_element()

driver.maximize_window()


driver.close()