import time
import re
import socket

import dota2api
import json
api = dota2api.Initialise('829F60173C0683A4DCC3C665FF8ED79F')
match = api.get_match_details(match_id='1000193456')
items = api.get_game_items()


sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('139.59.61.220',6666))
#FLag ALEXCTF{1_4M_l33t_b0t}
count=0;
while True:
        recipe=sock.recv(1024)
	
	if "xiomara" in recipe:
		break
	print recipe
	da = recipe.split('\n')
	print "--------------"
	if da==['']:
		break
	print da
	for row in da:
		if 'Can haz cost of Recipe' in row:
			print "inside recipe"
			rec = row.split(':')[1].strip()[:-1].strip()
			weapon = filter(lambda i: i['localized_name'] == 'Recipe: '+rec, items['items'])[0]
			price = str(weapon['cost']).replace(' ','')
			print sock.send(price+'\r\n')
			
		elif 'Can haz cost of ' in row: 
			data3 = row.split('Can haz cost of ')[1].strip()[:-3].strip()
			weapon = filter(lambda i: i['localized_name'] == data3, items['items'])[0]
			tw = str(weapon['cost']).replace(' ','')
			print sock.send(tw+'\r\n')
		
		elif 'Can haz internal name of Recipe' in row:
			name = row.split(':')[1].strip()[:-1].strip()
			print name
			weapon1 = filter(lambda i: i['localized_name'] == 'Recipe: '+rec, items['items'])[0]
			name2 = str(weapon1['name'].encode('utf-8')).strip()+'\r'
			print name2
			print sock.send(name2.encode()+'\n')

		elif 'Can haz internal name of ' in row:
			dname = row.split('Can haz internal name of ')[1].strip()[:-3].strip()
			print dname
			weapon2 = filter(lambda i: i['localized_name'] == dname, items['items'])[0]
			twname = str(weapon2['name'].encode('utf-8')).strip()+'\r'
			print twname
			print sock.send(twname.encode()+'\n')
