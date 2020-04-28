###################################################################
## ROTATING PROXIES
###################################################################
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random

def clearScreen():
  print(chr(27)+'[2j')
  print('\033c')
  print('\x1bc')

ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port] 

# Retrieve latest proxies
myRequest = Request('https://www.worldometers.info/coronavirus/')
myRequest.add_header('User-Agent', ua.random)
myRequest_doc = urlopen(myRequest).read().decode('utf8')

soup = BeautifulSoup(myRequest_doc, 'html.parser')
content_table = soup.find(id='main_table_countries_today')

####################################################################

def main():  
  clearScreen()
  print ('COVID Dump')
  print ('####################################'+'\n')

  print (content_table)

if __name__ == "__main__":
      main()
