import requests
import numpy as np
from datetime import datetime
from config import SOLARJOBS_BASIC_URL, SOLARJOBS_DETAIL_URL

DATE_FORMAT = "%m.%d.%Y"

r_basic = requests.get(SOLARJOBS_BASIC_URL).json()
r_detail = requests.get(SOLARJOBS_DETAIL_URL).json()

basic_col = r_basic['results']['collection1']
detail_col = r_detail['results']['collection1']


titles = []
for x in basic_col:
	try:
		titles.append(x['solarjobs_title']['text'])
	except:
		pass

links = []
for x in basic_col:
	try:
		links.append(x['solarjobs_title']['href'])
	except:
		pass

companies = []
for x in basic_col:
	try:
		companies.append(x['solarjobs_company']['text'])
	except:
		pass

dates = []
for x in basic_col:
	try:
		dates.append(datetime.strptime(x['solarjobs_date'],  DATE_FORMAT))
	except:
		pass

locations = []
for x in detail_col:
	try:
		locations.append(x['solarjobs_location'])
	except:
		pass


#titles = [x['solarjobs_title']['text'] for x in r_basic['results']['collection1']]
#links = [x['solarjobs_title']['href'] for x in r_basic['results']['collection1']]
#companies = [x['solarjobs_company']['text'] for x in r_basic['results']['collection1']]
#dates = [datetime.strptime(x['solarjobs_date'], DATE_FORMAT) for x in r_basic['results']['collection1']]
#locations = [x['solarjobs_location'] for x in r_detail['results']['collection1']]

'''
index: category
0: titles
1: companies
2: locations
3: dates
4: links
'''

solarjobs_jobs = np.array([titles, companies, locations, dates, links]).transpose()

