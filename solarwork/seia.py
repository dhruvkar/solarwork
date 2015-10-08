import requests
import numpy as np
from datetime import datetime
from config import SEIA_URL

DATE_FORMAT = "%m/%d/%Y"

r = requests.get(SEIA_URL).json()
col = r['results']['collection1']

#titles = [x['seia_title']['text'] for x in r['results']['collection1']]
#links = [x['seia_title']['href'] for x in r['results']['collection1']]
#companies = [x['seia_company']['text'] for x in r['results']['collection1']]
#dates = [datetime.strptime(x['seia_date']['text'],  DATE_FORMAT)for x in r['results']['collection1']]
#locations = [x['seia_location']['text'] for x in r['results']['collection1']]

titles = []
for x in col:
	try:
		titles.append(x['seia_title']['text'])
	except:
		pass

links = []
for x in col:
	try:
		links.append(x['seia_title']['href'])
	except:
		pass

companies = []
for x in col:
	try:
		companies.append(x['seia_company']['text'])
	except:
		pass

dates = []
for x in col:
	if x['seia_date']['text']:
		dates.append(datetime.strptime(x['seia_date']['text'],  DATE_FORMAT))

locations = []
for x in col:
	if x['seia_location']['text']:
		locations.append(x['seia_location']['text'])



'''
index: category
0: titles
1: companies
2: locations
3: dates
4: links
'''

seia_jobs = np.array([titles, companies, locations, dates, links]).transpose()
