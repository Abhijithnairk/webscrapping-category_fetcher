import pandas as pd
import numpy as np
import json
from colorama import*
import requests

with open('category_wise_scrapping.json','r') as file:
    competitor_list = json.load(file).get("competitor_list")
    
row_data={}
for competitor in competitor_list:
    row_data.update({competitor.get('name'):[]})
    
for competitor in competitor_list:
    print(Fore.GREEN+"fetching data from "+competitor.get('name'))
    URL=competitor.get('cat_url')
    cookie=competitor.get('cookie')
    HEADERS={
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            'Cookie': cookie 
    }


    responces=requests.get(URL,headers=HEADERS)
    #if responces.status_code==200:
    data=responces.json()
    items=data.get('items')
    for item in items:
        row_data[competitor.get('name')].append(item.get('name'))
        #print(Style.BRIGHT + Fore.GREEN + "category data fetched\n")   
    


maxlength=max(len(arr) for arr in row_data.values())

#print(len(row_data['sprouts']))
#print(len(row_data['wegmans']))
#print(len(row_data['fresh mart'])) 

for key,value in row_data.items():
    #print(f"name is :{key} length{len(value)}")
    if len(value)<maxlength:
        row_data[key]=value+[np.nan]*(maxlength-len(value))
        
#print(row_data)
df=pd.DataFrame(row_data)
print(df)
output=df.to_excel("category.xlsx",index=False)
print(output)
      
