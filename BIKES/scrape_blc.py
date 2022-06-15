import csv
import requests
from datetime import datetime
from pytz import timezone

def localtime():
    scl_time = datetime.now(timezone('America/Santiago'))
    return scl_time.strftime('%Y-%m-%d %H:%M:%S')

url='http://bicilascondes.cl/availability_map/getJsonObject'
json=requests.get(url).json()

cols=json[0].keys()
OFF_COLS = ['zip','address','addressNumber','nearbyStations','district']
# add: NAME+STATUS??
cols=[c for c in cols if c not in OFF_COLS]+['time']

loc = localtime()
print('TIME:', loc)

with open('stats.csv','a') as fw:
    sw = csv.writer(fw, quotechar='"')
    for jix in json:
        fjix = jix.copy()
        fjix['time'] = loc
        #vals=','.join([fjix[k] for k in cols])
        vals=[fjix[k] for k in cols]
        print(vals)
        sw.writerow(vals)
        del fjix
        del vals
