import arrow
import requests
import numpy as np
from datetime import datetime


#DATE_FORMAT = "%m/%d/%Y"

r = requests.get(BRIGHTCURRENT_URL).json()


titles = [x['brightcurrent_title']['text'] for x in r['results']['collection1']]
links = [x['brightcurrent_title']['href'] for x in r['results']['collection1']]
companies = 'BrightCurrent'
dates = [x['brightcurrent_date'] for x in r['results']['collection1']]
locations = [x['brightcurrent_location'] for x in r['results']['collection1']]

'''
index: category
0: titles
1: companies
2: locations
3: dates
4: links
'''

#brightcurrent_jobs = np.array([titles, companies, locations, dates, links]).transpose()