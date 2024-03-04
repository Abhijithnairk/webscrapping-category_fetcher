import pandas as pd
import requests
import json
from colorama import*

with open('category_wise_scrapping.json','r') as file:
    competitor_list=json.load(file).get('competitor_list')
    
    
searchterm=input("Enter the item to search: ")
searchterm=searchterm.lower()


for competitor in competitor_list:
    print(Style.BRIGHT+Fore.YELLOW+competitor.get('name'))
    cookie=competitor.get('cookie')
    HEADERS={
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            'Cookie': cookie 
    }
    URL=competitor.get('store_api')+searchterm
    responces=requests.get(URL,headers=HEADERS)
    data=responces.json()
    #print(data)
    items=data.get('items')
    #print(items[0]['name'])
    
    for item in items:
        if (searchterm in item.get('name').lower()):
            print(Style.BRIGHT+Fore.BLUE+item.get('name'))
            for category in item.get('categories'):
                print(Style.BRIGHT+Fore.CYAN+category.get("name"))
                
            print("---------------------------")
        
    
    