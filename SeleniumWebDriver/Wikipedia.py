from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_driver_path = "/Adi/UdemyPython/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(0.5)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

todays_article = driver.find_element(by=By.ID ,value="From_today's_featured_article")
# print(todays_article.text)

search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.submit()

# driver.quit()