import requests 
import json 


"""Key Columns
-> Eccentricity: Iregularity of Planetary Orbit (Non Circle)
"""


BASE_URL = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query='
QUERY = 'SELECT+*+FROM+TD'


r = requests.get(f'{BASE_URL}{QUERY}')

print(r.status_code)
