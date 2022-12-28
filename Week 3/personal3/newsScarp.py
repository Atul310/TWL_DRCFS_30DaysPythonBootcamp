
import bs4
import requests
from datetime import datetime
## it us not alloweded to scrape any website without the permisiion if the 
## we should check the robots.txt in order to scrape the data 
## 
def Url_request(url:str)-> str:
	return requests.get(url="").text

def parse_html(Unparsedhtml:str)-> bs4.BeautifulSoup:
	return bs4.BeautifulSoup(Unparsedhtml,"htmlparser")

def get_detail_fromSoup(soup:bs4.BeautifulSoup)-> str:
	price_Element = soup.find("",)
	priceNepali=price_Element
	return priceNepali

def Write_file(price:str, filename:str):
	with open(filename ,mode='a',encoding='') as file :
		file.write(price)
		file.write("\n")

