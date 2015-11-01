import json
import requests
import requests_cache
import datetime
import numpy as np
import arrow
from flask import Flask, render_template
from config import *
from seia import *

# Create cache
requests_cache.install_cache('kimonolabs_cache', backend='sqlite', expire_after=180)
#from seia import seia_jobs
#from solarjobs import solarjobs_jobs 


# Initialize app
app = Flask(__name__)

# A function/template filter to format the dates
@app.template_filter()
def format_date(date_str):
    try:
        date_str = arrow.get(date_str).humanize()
    except:
        pass
    return date_str

app.jinja_env.filters['format_date'] = format_date


# Define homepage to display jobs
@app.route('/')
def jobs():
    titles = get_titles(SEIA_URL)
    companies = get_companies(SEIA_URL)
    locations = get_locations(SEIA_URL)
    dates = get_dates(SEIA_URL)
    links = get_links(SEIA_URL)
    seia_jobs = create_np_array([titles, companies, locations, dates, links])
    alljobs = np.concatenate([seia_jobs])
    alljobs = alljobs[alljobs[:,3].argsort()[::-1]]

    return render_template('jobs.html', alljobs=alljobs)

# Subscribe page with embedded Mailchimp form
@app.route('/subscribe/')
def subscribe():
    return render_template('subscribe.html')

# Post Job page
#@app.route('/post/')
#def post_job():
# //TO DO


# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
