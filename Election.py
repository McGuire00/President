import requests
from bs4 import BeautifulSoup
from datetime import datetime
import time

def clock():
    current = datetime.now()
    return(str(current) + " EST")

clock()
headers = {
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9'
}

url = 'https://www.yahoo.com/elections'

def president():
    while True:
        page = requests.get(url, headers=headers)

        soup = BeautifulSoup(page.text, 'html.parser')


        for info in soup.find_all('div', attrs={"class":"balance balance--presidential balance--counting"}):
            percent = info.find_all('div', class_="balance__below")
            #Gets percentage of Biden votes
            joe_percent = percent[0].find_all('span')[0].text
            joe_votes = percent[0].find_all('span')[1].text

            # Gets percentage of Trump votes
            donald_percent = percent[0].find_all('span')[3].text
            donald_votes = percent[0].find_all('span')[2].text
            #print(percent)

            # Gets Biden name and electoral votes
            biden = info.find_all("div", class_="side__content")[0]
            biden_name = biden.find("div").text
            biden_elect = biden.find(class_="side__num").text

            #Gets trump name and electoral votes
            trump = info.find_all("div", class_="side__content")[1]
            trump_name = trump.find("div").text
            trump_elect = trump.find(class_="side__num").text

            print(clock(), '::: The candidates need 270 electoral votes to win')
            print(clock(), ':::',biden_name, 'has',biden_elect,'electoral votes with',joe_percent, 'of the popular vote and', joe_votes, 'total')
            print(clock(), ':::',trump_name, 'has',trump_elect,'electoral votes with',donald_percent, 'of the popular vote and', donald_votes, 'total')
            #refeshes page every 30 seconds
            time.sleep(30)
            print()
president()
