import json
import requests
import requests_cache
import datetime
import numpy as np
import arrow
from flask import Flask, render_template

# Create cache
requests_cache.install_cache('kimonolabs_cache', backend='sqlite', expire_after=1800)
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
    from seia import seia_jobs
    from solarjobs import solarjobs_jobs 
    alljobs = np.concatenate([seia_jobs])
    alljobs = alljobs[alljobs[:,3].argsort()[::-1]]

    return render_template('jobs.html', alljobs=alljobs)

# Subscribe page with embedded Mailchimp form
@app.route('/subscribe/')
def subscribe():
    return render_template('subscribe.html')

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
