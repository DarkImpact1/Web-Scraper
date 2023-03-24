from bs4 import BeautifulSoup
import requests
from csv import writer
url = 'https://bit.ly/3z8m1DT'


r = requests.get(url)
soup = BeautifulSoup(r.content,'html.parser')
mobile_list = soup.find_all('div',class_='_2kHMtA')
with open('mobiles_under_30k.csv','w', encoding='utf-8',newline='') as file:
    thewriter = writer(file)
    header = ['Mobile Name', 'Price', 'Exchange Offer', 'RAM & ROM', 'Processor','Display', 'Camera', 'Battery', 'warranty']
    thewriter.writerow(header)
    for mobiles in mobile_list:
        mobile_name = mobiles.find('div',class_='_4rR01T').text
        mobile_price = mobiles.find('div',class_='_30jeq3 _1_WHN1').text.replace("â‚","")
        if mobiles.find('div',class_='_3xFhiH'):
            exchange_offer= mobiles.find('div',class_='_3xFhiH').text.replace("â‚","")
        else:
            exchange_offer=""
        spec = mobiles.find('li',class_='rgWa7D').text
        display = mobiles.find('li',class_='rgWa7D').nextSibling.text
        camera = mobiles.find('li',class_='rgWa7D').nextSibling.nextSibling.text
        battery = mobiles.find('li',class_='rgWa7D').nextSibling.nextSibling.nextSibling.text
        processor = mobiles.find('li',class_='rgWa7D').nextSibling.nextSibling.nextSibling.nextSibling.text
        if mobiles.find('li',class_='rgWa7D').nextSibling.nextSibling.nextSibling.nextSibling.nextSibling:
            warranty = mobiles.find('li',class_='rgWa7D').nextSibling.nextSibling.nextSibling.nextSibling.nextSibling.text
        else:
            warranty=""
        information = [mobile_name, mobile_price, exchange_offer,spec,processor,display,camera,battery,warranty]
        thewriter.writerow(information)

