import requests
import smtplib
import os.path

# ---------------------------------------- Stock Price API ------------------------------------------ #
stock_price_url = "https://www.alphavantage.co/query"
api_key = "Z2JRWM8JZH99SMRG"
symbol = "AAPL"
count = 0

parameters = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : symbol,
    "apikey" : api_key
}

response = requests.get(stock_price_url,params=parameters)
response.raise_for_status()
stock_price = response.json()
stock_price_list = list[stock_price]

last_refreshed_date = stock_price["Meta Data"]["3. Last Refreshed"]
timezone = stock_price["Meta Data"]["5. Time Zone"]
day_before_date = "2023-07-03"

most_recent_closing_price = stock_price["Time Series (Daily)"][last_refreshed_date]["4. close"]
day_before_closing_price = stock_price["Time Series (Daily)"][day_before_date]["4. close"]

percentage_change = round((float(most_recent_closing_price)-float(day_before_closing_price))/float(day_before_closing_price) * 100,2)

# ------------------------------------ Get News API -------------------------------------------- #
news_api_key = "aab11b3edbcb4092beb5aaba3d9f2c40"
news_url = "https://newsapi.org/v2/everything"
news_parameters = {
    "q" : symbol,
    "apikey" : news_api_key,
    "sortBy" : "publishedAt",
    "language" : "en"
}

news_response = requests.get(news_url,news_parameters)
news = news_response.json()

if os.path.isfile(f"/Adi/PythonCodes/Stock_News/{symbol}_News.txt") == True :
    with open(f"/Adi/PythonCodes/{symbol}_News.txt","w") as news_file :
        news_file.write(f'''
Stock Name : {symbol}
Most recent closing price : {most_recent_closing_price}
Day before closing date : {day_before_closing_price}
Percentage Change : {percentage_change} 
Timezone : {timezone}
    ''')
else :
    with open(f"/Adi/PythonCodes/Stock_News/{symbol}_News.txt","a") as news_file :
            news_file.write(f'''
    Stock Name : {symbol}
    Most recent closing price : {most_recent_closing_price}
    Day before closing date : {day_before_closing_price}
    Percentage Change : {percentage_change} 
    Timezone : {timezone}
        ''')

def get_News() :
    global count
    global symbol
    global closing_price
    
    ID_name = news["articles"][count]["source"]["name"]
    author = news["articles"][count]["author"]
    title = news["articles"][count]["title"]
    description = news["articles"][count]["description"]
    url = news["articles"][count]["url"]
    
    with open(f"/Adi/PythonCodes/Stock_News/{symbol}_News.txt","a") as news_file :
        news_file.write(f'''
Id_Name : {ID_name}
Author : {author}
Title : {title}
Description : {description}
URL : {url}
''')

    count+=1


for i in range(4) :
    get_News()


# ------------------------------------- Send Mail ------------------------------------------------- #

with open(f"/Adi/PythonCodes/Stock_News/{symbol}_News.txt","r") as read_news_file :
    all_news = read_news_file.read()

email = "chaditya789@gmail.com"
password = "rlviotwrmmwomwez"
to_address = "chaditya972@gmail.com"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=email,password=password)
connection.sendmail(from_addr=email,to_addrs=to_address,msg=f"Subject: Report on {symbol} stock\n\n{all_news}".encode("utf-8"))
connection.close()