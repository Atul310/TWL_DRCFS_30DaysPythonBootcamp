import bs4
import requests
import urllib

## Go to daraz for specific product 
## fetch its current price 
## write the price to a file for every 60 sec

#==============
##request daraz product page using request module 
## parse the html string using bs4
## find the elements that contains the price 
## convert the price int integer 
## write the price in a file 


## At first we request the url  which is in string and it return the string -> menas it return string

def request_site(url: str)->str:   
    return requests.get(url,timeout=1000).text   ## it request return from .text attribute


## it returns in the form of soup in python object like
def parse_html(unparsed_html:str)->bs4.BeautifulSoup:
    return bs4.BeautifulSoup(unparsed_html,"html.parser")  

    
 # html parser is a thing to convert html to python
## We have parsed html parser in string 

## We get price in the form of soup and we 
## soup is 
def get_price_From_soup(soup:bs4.BeautifulSoup)->float:
    price_elemet = soup.find('class=product-info pdpWrapper')
    return price_elemet

def Write_price_to_file(price: str, filename: str) :
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(price)
        file.write('\n') 
'''    
## use of main function is used to 
#1request the site 
'''
def main():
 websit_url = "https://www.sastodeal.com/indpro-legend-football-shoes-orange-sd-275646-1381-rkolay-c1106-001.html" ## reuest site url
 file_path ="data.txt"
 html_str = request_site(websit_url)
 soup =  parse_html(html_str) ## parsing html 
 price =get_price_From_soup(soup)
 Write_price_to_file(price,file_path)

if __name__ == '__main__':
    main();
### 