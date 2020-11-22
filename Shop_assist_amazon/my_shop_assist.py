#used libraries
import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import time
import csv
import os
from twilio.rest import Client

#function that sends whatsapp alert to my phone whenever the product is at/below my desired price
def whatsapp_alert(alert):
    client = Client()
    print(os.environ['MY_PHONE_NUMBER'])
    from_whatsapp_number = 'whatsapp:+14155238886'
    to_whatsapp_number = 'whatsapp:' + os.environ['MY_PHONE_NUMBER']

    client.messages.create(body=alert,
                           from_=from_whatsapp_number,
                           to=to_whatsapp_number)

#main web scrapper function that assists us to grab and compare data using beuatiful soup and csv libraries
def get_price():
    #reading the saved csv file for item links and desired price
    file = pd.read_csv('items_list.csv', sep=',')
    urls = file.url
    #loop iterating through each row
    for row, url in enumerate(urls):
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        #exact instance of time in IST
        lookup_time = time.strftime('%Y-%m-%d %Hh%Mm')

        link = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(link, 'html.parser')

        #using try and error because the title/price of different products could be listed under different ids
        try:
            title = soup.find(id="productTitle").get_text().split()
        except:
            title = None

        try:
            price = soup.find(id="priceblock_dealprice").get_text().split()
        except:
            price = None
        if price == None:
            try:
                price = soup.find(id="priceblock_ourprice").get_text().split()
            except:
                try:
                    price = soup.find(id="priceblock_saleprice").get_text().split()
                except:
                    price = None
        article_title = " ".join(title)

        #if price is retrieved from the amazon website
        if price != None:

            #obtaining the float value of price for comparison
            article_price = float(price[1].replace(",", ""))

            #condition for comparing the price to our desired price for the product
            if article_price <= file.desired_price[row]:
                alert_message = "*****BUY NOW: " + article_title + " at Rs." + str(article_price) + " *****"

                #function to send alert to my phone called
                whatsapp_alert(alert_message)
                print(alert_message)

            else:
                alert_message = "NA"
            print(article_title, ": ", article_price)

            #saving the obtained data logs everytime the code is run into a excel file
            with open("search_results.csv", 'a', newline='') as f:
                w = csv.writer(f, dialect='excel')
                result = [article_title, str(article_price), str(lookup_time), alert_message]
                w.writerow(result)

        #incase the web scrapper is not able to obtain the price of the article (mostly due to unavailability)
        else:
            print("Price of this article was not found")
            with open("search_results.csv", 'a', newline='') as f:
                w = csv.writer(f, dialect='excel')
                w.writerow([article_title, 'NA', str(lookup_time), "item price not found!"])

#main web scrapper called
get_price()
