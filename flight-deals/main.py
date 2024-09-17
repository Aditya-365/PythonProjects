import requests
import os.path 

# ----------------------------------------- CONSTANTS ----------------------------------------------- #
api_key = "u8yyoRe4V3xU0fU38E9ww_IZbT843xIY"
departure = "BLR"
destination = "DFW"
date_from = "09/07/2023"
date_to = "20/07/2023"
return_from = "01/09/2023"
return_to = "08/09/2023"
cabin = "M"
maximum_price = 2000
currency = "USD"
limit_searches = 5
count = 0
# ----------------------------------------- FLIGHT SEARCH ------------------------------------------- #

search_url = "https://api.tequila.kiwi.com/v2/search"

search_params = {
    "fly_from" : departure,
    "fly_to" : destination,
    "date_from" : date_from,
    "date_to" : date_to,
    "return_from" : return_from,
    "return_to" : return_to,
    "selected_cabins" : cabin,
    "price_to" : maximum_price,
    "curr" : currency,
    "limit" : limit_searches
}

header = {
    "apikey" : api_key
}

response = requests.get(url=search_url,params=search_params,headers=header)
flight_data = response.json()
print(flight_data)

# -------------------------------- STORING DATA ------------------------------------------------------ #
if os.path.isfile(f"/Adi/PythonCodes/flight-deals/{departure}-{destination}.txt") :
    with open(f"/Adi/PythonCodes/flight-deals/{departure}-{destination}.txt","w") as read_filght_data :
        pass
else :
    with open(f"/Adi/PythonCodes/flight-deals/{departure}-{destination}.txt","a") as read_filght_data :
        pass


for i in range(0,limit_searches) : 
    flight_departure = flight_data["data"][count]["cityCodeFrom"]
    flight_to = flight_data["data"][count]["cityCodeTo"]
    price = flight_data["data"][count]["price"]
    available_seats = flight_data["data"][0]["availability"]
    stops = flight_data["data"][count]["pnr_count"] 
    airlines = flight_data["data"][count]["airlines"]
    route_city1 = flight_data["data"][count]["route"][0]["cityTo"]
    route_city2 = flight_data["data"][count]["route"][1]["cityTo"]
    id = flight_data["data"][count]["id"]
    with open(f"/Adi/PythonCodes/flight-deals/{departure}-{destination}.txt","a") as read_filght_data :
        flights = read_filght_data.write(f'''
{count}.
ID : {id}
Flight From : {flight_departure}
Flight To : {flight_to}
Price : {price}
Available Seats : {available_seats}
No. of Stops : {stops}
Airlines : {airlines}
Route Via {route_city1} & {route_city2}''')
    count+=1