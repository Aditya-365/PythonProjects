from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time 

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get("https://www.zillow.com/arlington-tx/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-97.31716555957031%2C%22east%22%3A-96.95324344042969%2C%22south%22%3A32.544036801080516%2C%22north%22%3A32.85951928905371%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A50763%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A2000%7D%2C%22price%22%3A%7B%22max%22%3A392703%7D%2C%22beds%22%3A%7B%22min%22%3A2%7D%2C%22baths%22%3A%7B%22min%22%3A1.5%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D",headers=header)
zillow_wp = response.text

soup = BeautifulSoup(zillow_wp,"lxml")
print(soup.title.text)

all_link_elements = soup.find_all(class_="StyledPropertyCardDataArea-c11n-8-89-0__sc-yipmu-0 gZUDVm property-card-link")

all_links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.find_all(name="address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.find_all(class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")
all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]

# ------------------------------------- OPENING GOOGLE FORMS ---------------------------------------- #

google_forms_link = "https://forms.gle/2VVDG1KaECrGMVLM9"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.implicitly_wait(0.5)

count = 0
for i in range(len(all_links)) :
    driver.get(google_forms_link)

    house_address = driver.find_elements(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    house_address.send_keys(all_addresses[count])

    house_rent = driver.find_elements(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    house_rent.send_keys(all_prices[count])

    house_link = driver.find_elements(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    house_link.send_keys(all_links[count])

    count += 1

    submit = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()
    

driver.find_element(by=By.LINK_TEXT, value="Responses")
google_sheets = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
google_sheets.click()