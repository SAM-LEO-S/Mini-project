import pandas as pd 
from alpha_vantage.timeseries import TimeSeries 

import matplotlib.pyplot as plt 
import time
import smtplib 
from twilio.rest import Client
from datetime import datetime, timedelta
from datetime import timedelta, date
import requests



stock_name = input("Enter the name of the stock:")
Limit=int(input("Enter your Limit::"))
ts = TimeSeries(key='K9VHHDQ753WTXHU4.', output_format='pandas')
data, meta_data = ts.get_intraday(symbol=stock_name,interval='1min', outputsize='full')



close_data = data['4. close']

last_price = close_data[0] 
print(last_price)

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "apikey": "K9VHHDQ753WTXHU4.",
    "function": "TIME_SERIES_DAILY",
    "outputsize": "compact"
}

news_params = {
    "apiKey": "8da182d5da71480b91098e48a37d5e3a"
}


try:
    yesterday = datetime.now() - timedelta(1)
    yesterday = datetime.strftime(yesterday, '%Y-%m-%d')
    previous_day = datetime.now() - timedelta(2)
    previous_day = datetime.strftime(previous_day, '%Y-%m-%d')



    # stock_value
    response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    stock_price = response.json()
    yesterday_price = float(stock_price["Time Series (Daily)"][yesterday]["4. close"])


    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    top_news = news_response.json()
    total_news = 3
    list_of_news = []
    for news_num in range(total_news):
            list_of_news.append(top_news["articles"][news_num]["title"])



    #
    sender_email = "industriesstark187@gmail.com" 
    rec_email = "leoosam00005@gmail.com" 
    password = ("grhjqpfpprvxiqgc")
    message = "HELLO BOSS..............STOCK ALERT!!! The stock is at above price you set "  +"="+ str(last_price) +"."+ "The yesterday's price for your observation" +"="+ str(yesterday_price) +"."
    target_sell_price = Limit
    account_sid = 'AC30f4e4a76855349d37ef0c9aec3a3c92'
    auth_token = 'd0b37507117aeec5c6b3cb6005c7e155'
        
    client = Client(account_sid, auth_token)

    if last_price > target_sell_price:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("industriesstark187@gmail.com", "grhjqpfpprvxiqgc") 
            print("Login Success")
            server.sendmail("industriesstark187@gmail.com", "leoosam00005@gmail.com", message) 
            print("Email was sent") 
    
            Message = client.messages.create(
                                    from_="+15303897966" ,
                                    body ="HELLO BOSS................STOCK ALERT!!! The stock is at above price you set " +"="+ str(last_price) +"."+ "The yesterday's price for your observation" +"="+ str(yesterday_price) +".",
                                    to ='+917010106545',
                                    
                                )

                                
except:
    sender_email = "industriesstark187@gmail.com" 
    rec_email = "leoosam00005@gmail.com" 
    password = ("grhjqpfpprvxiqgc")
    message = "HELLO BOSS..............NSE or National Stock Exchange is open on the weekdays from Monday to Friday and is closed on Saturday and Sunday, except any special trading sessions are announced."
    target_sell_price = Limit
    account_sid = 'AC30f4e4a76855349d37ef0c9aec3a3c92'
    auth_token = 'd0b37507117aeec5c6b3cb6005c7e155'
        
    client = Client(account_sid, auth_token)

    if last_price > target_sell_price:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("industriesstark187@gmail.com", "grhjqpfpprvxiqgc") 
            print("Login Success")
            server.sendmail("industriesstark187@gmail.com", "leoosam00005@gmail.com", message) 
            print("Email was sent") 
    
            Message = client.messages.create(
                                    from_="+15303897966" ,
                                    body ="HELLO BOSS..............NSE or National Stock Exchange is open on the weekdays from Monday to Friday and is closed on Saturday and Sunday, except any special trading sessions are announced.",
                                    to ='+917010106545',
                                    
                                )


    