import bs4
import requests
import urllib.request
from bs4 import BeautifulSoup as soup
## visit website 
## to open the website in python we use 
## a library called {urllib}

from  urllib.request import urlopen

## urlopen ==>> 
## reading the url 
data =urlopen ("https://www.flipkart.com/6bo/b5g/~cs-yb0defth0m/pr?sid=6bo%2Cb5g&collection-tab-name=Browsing&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkJyb3dzaW5nIExhcHRvcHMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=24.productCard.PMU_V2_2") ## it opens the information of all prdouct by urlopen 
dataStore= data.read() ## reading  data from the above function and storing it in a varible called datastore

#print(dataStore) ## it prints the all content 
soupdata =soup(dataStore) ## 
dir(soupdata)

Containers =soupdata.findAll("div",{"class":"_2kHMtA"})
Containers[0]