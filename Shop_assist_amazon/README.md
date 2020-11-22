# Shop_Assit_Amazon
 a program to assist my shopping habit by scraping my desired product details from Amazon.in and sending me alerts whenever my conditions are met.
 
 Due to the circumstances which were caused due to the outbreak of Covid-19, this whole world was pushed online for its daily functioning, we all saw a rise in our online activity, whether it is work and study related or for our past time.

 The same happened to me, with most of the shopping moved online,I found myself at the amazon.in website looking for things and articles that I wanted to buy, I developed a    tendency to check for the prices and observed that the prices of the things that I wanted to buy changed frequently and the things were available at diferent prices during different times if the week, so having a desire to get the stuff that I want at a price that is suitable to me, I started visiting the amazon site. I soon realised that I visited  it more often than enough just to check on the prices of the things that I wanted to buy, which isn't good both practically and physically as it is time consuming and often hectic if you are a person like me who wants to get a lot of stuff.

 So then I came across an article on how to scrape web data using python, like this thing wasn't new to me as I had previously studied about web crwaling and stuff related to it when I learned python. So this gave me a thought to make a web scraper for amazon and then I started searching for some articles for refrences and came across this beautiful article and code done by Fabio Neves on how to scrape amazon for price alerts (linked: https://towardsdatascience.com/scraping-multiple-amazon-stores-with-python-5eab811453a8), so using his idea as refrence I started working on my project, which took me like a day to finsih initially with the web scraping through beautiful soup and getting prices, but I struggled on the price alert part as it was new to me and initially my code failed due to circular import.
 
 So here is my approach to this project, I divided it into 3 parts and used them in my self defined function "get_prices":
 1. Web scraping of pricing through Beautiful Soup library use
 2. Comparison of retrieved price from my desired price for the product
 3. Sending a whatsapp alert directly to my phone when my conditions are met (in self defined function "whatsapp_alert")
 

1. Web scraping of pricing through Beautiful Soup library use:
 I use the bs4 library to use the Beautifulsoup function which helps me retrieve id specific text which contain prices of the aricles that I search for, these prices are then converted to float calues for comparison. These prices are obtainedas the url is feeded through the csv file named "items_list.csv" which contains the url and desired price for the particular item. each item is iterated through when the function is called and each link is scraped using the Beautifulsoup function. I use 'try and except' everytime I search for the price of the product because different product prices are listed under certain different ids, which I observed using the inspect elemnt feature in chrome, which allows you to see the respective HTML code, now remeber beautifulsoup allows you to obtain the HTML data of a webpage and get the various tags and text data. So it made it all easy.   
 
2.Comparison of retrieved prices from the desired price for the product:
 I use simple conditional statements to compare the price that I obtained by scraping the item link read from the csv file, now the price that I recieve is in string form and contains charactes such as Currency symbol and commas, so I firstly separate it obtain the price as a float value and compare it to the desired price that I again read from the csv file used here. If the price is lower or equal to the desired value I generate an alert message and then move forward to send me a whatsapp alert to my phone, so that I maybe instantly able toa access the article at that price, this alert is not generated and sent of the listed condition is not met. This whole retrieval is saved into an excel file named "searched_results.csv" with columns such as article name, price, time of retrieval, and alerts.
 
3. Sending a whatsapp alert directly to my phone when my conditions are met (in self defined function "whatsapp_alert"):
 Now if the article is at a price lower or equal to my desired price, I use the self defined function "whatsapp_alert" to send myself an alert message, here I use the twilio API to help me send an alert message to my whatsapp phone number (saved in environment and accessed using os), twilio is a really handy API which allows one to send a message to (a) listed number(s) using only few lines of code, you can learn furthur about sending message through twilio using this youtube video(linked: https://www.youtube.com/watch?v=98OewpG8-yw)
 
So after completing this code and it running fully, I was really elated as I was able to solve my daily problem using python so easily. I look forward to do such projects more often as I learned a lot while doing this one, I hope you liked it!
Thank You!
