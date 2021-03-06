import requests
import numpy as np
from datetime import datetime

def get_titles(url):
    titles = []
    collection = requests.get(url).json()['results']['collection1']
    for x in collection:
        try:
            titles.append(x['seia_title']['text'])
        except:
            pass
    return titles

def get_links(url):
    links = []
    collection = requests.get(url).json()['results']['collection1']
    for x in collection:
        try:
            links.append(x['seia_title']['href'])
        except:
            pass
    return links

def get_companies(url):
    companies = []
    collection = requests.get(url).json()['results']['collection1']
    for x in collection:
        try:
            companies.append(x['seia_company']['text'])
        except:
            pass
    return companies

def get_dates(url):
    DATE_FORMAT = "%m/%d/%Y"
    dates = []
    collection = requests.get(url).json()['results']['collection1']
    for x in collection:
        try:
            #x['seia_date']['text']:
            dates.append(datetime.strptime(x['seia_date']['text'],  DATE_FORMAT))
        except:
            pass
    return dates

def get_locations(url):
    locations = []
    collection = requests.get(url).json()['results']['collection1']
    for x in collection:
        try:
            locations.append(x['seia_location']['text'])
        except:
            pass
    return locations




'''
index: category
0: titles
1: companies
2: locations
3: dates
4: links
'''
def create_np_array(list_of_stuff):
    arr = np.array(list_of_stuff).transpose()
    return arr

#seia_jobs = np.array([titles, companies, locations, dates, links]).transpose()
