#################################################################################
#
#
#
#################################################################################
import os
import sys
import requests
from bs4 import BeautifulSoup
import urllib

MONEYURL = "www.moneycontrol.com"
moneydata = requests.get("http://" + MONEYURL)

moneydata = moneydata.text

soup = BeautifulSoup(moneydata)

#for link in soup.find_all('a'):
#    print(link.get('href'))

post_params = {'param1': 'JKTYRE'}
post_args = urllib.urlencode(post_params)

fp = urllib.urlopen(MONEYURL, post_args)
soup2 = BeautifulSoup(fp)
print(soup2)