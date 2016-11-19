##########################################################################
#
#
##########################################################################

import os
import os.path
import sys
from bs4 import BeautifulSoup
import urllib
import requests
import re
import lxml

STOCKURL = "http://www.moneycontrol.com/india/stockpricequote/auto-ancillaries/mothersonsumisystems/MSS01"

STOCKURL = requests.get(STOCKURL)

STOCKDATA = STOCKURL.text
soup = BeautifulSoup(STOCKDATA, "lxml")

## creating temporary file to store the hyperlinks
CURRPATH = os.getcwd()
TEXTFILE = os.path.join(CURRPATH, 'linkstorage.txt')

if os.path.isfile(TEXTFILE):
    os.remove(TEXTFILE)

filehand = open(TEXTFILE, 'w')

## dictionary to store urls
FINCLINKS = dict()
RAWLINKS = list()

STOCKLINKS = soup.find_all('a')

#print STOCKLINKS
for link in STOCKLINKS:
    eachlink = link.get('href')
    eachlink = str(eachlink)
    if re.match(r'\/financials', eachlink):
        if re.search(r'\/financials.*\/profit-lossVI\/.*', eachlink):
            FINCLINKS['profit-loss'] = eachlink
        elif re.search(r'\/financials.*\/balance-sheetVI\/.*', eachlink):
            FINCLINKS['balance-sheet'] = eachlink

for i in FINCLINKS:
    print FINCLINKS[i]
