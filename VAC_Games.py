#!/usr/bin/env python
 
import urllib.request
import re
from io import BytesIO
from bs4 import BeautifulSoup

steampage = BeautifulSoup(urllib.request.urlopen('http://store.steampowered.com/search/?category1=998&category2=8').read())
blacklist = open('blacklist.txt', 'w')
max_page = int(steampage.find('div', class_="search_pagination_right").find_all("a")[-2].string)
cuenta = 0

for page in range(1, max_page):
	if page != 1:
		steampage = BeautifulSoup(urllib.request.urlopen('http://store.steampowered.com/search/?category1=998&category2=8&page=' + str(page)).read())
	for row in steampage('a', href = re.compile(r'http://store.steampowered.com/app/*')):
		steamGameName = row.find('span', {'class' : 'title'})
		if steamGameName is not None:
			steamAppID = row.img.get('src').split("/")[5]
			blacklist.write('{0} || {1}, {2}\n'.format(cuenta, steamGameName.string, steamAppID))
			print('{0} || {1}, {2}\n'.format(cuenta, steamGameName.string, steamAppID))
			cuenta = cuenta + 1
 
blacklist.close()