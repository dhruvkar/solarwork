#solarwork.org

Solar job aggregator

To run:

**Make sure Vagrant and Ansible are installed.**
1. git clone https://github.com/dhruvkar/solarwork.git
1. Add a config.py file to solarwork/solarwork/ and define kimonolabs API endpoints.
1. `vagrant up`
1. `vagrant ssh`
1. `pip install -r requirements`
1. `cd solarwork`
1. `python quickstart`

You should now be able to see the site by going to "localhost:5000"
