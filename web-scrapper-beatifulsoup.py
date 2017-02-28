import time
import re
import socket
import requests
from bs4 import BeautifulSoup 
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
data2 = 'Can haz cost of Ring of Protection ? :'
r = requests.get('http://dota2.gamepedia.com/Items')
data = r.text
soup = BeautifulSoup(data, 'lxml')
recipe = 'Can haz cost of Recipe: Guardian Greaves ? :'
da = recipe.split(':?')
if len(da) > 1:
	rec = da[1].strip()[:-1].strip()
	for link in soup.findAll('a',title=lambda x: x and x.startswith(rec+' (')):
	    print str(link['title']).split('(')[1][:-1]
else:
	da = data2.split(':')
	data3 = da[0].split('Can haz cost of ')[1].strip()[:-1].strip()
	for link in soup.findAll('a',title=lambda x: x and x.startswith(data3+' (')):
    		print str(link['title']).split('(')[1][:-1]
