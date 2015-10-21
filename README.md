#solarwork.org

Solar job aggregator

To run:

**Make sure Vagrant and Ansible are installed.**

 1. git clone https://github.com/dhruvkar/solarwork.git
 1. Add a config.py file to solarwork/solarwork/ and define kimonolabs API endpoints.
 1. `cd solarwork && vagrant up`
 1. `vagrant ssh`
 1. `cd /dev/solarwork`
 1. `sudo pip install -r requirements.txt`
 1. `python quickstart.py`

You should now be able to see the site by going to "localhost:5000"
