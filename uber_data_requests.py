from uber_rides.session import Session
from uber_rides.client import UberRidesClient
import csv
import requests
import grequests
from gevent import monkey as curious_george
curious_george.patch_all(thread=False, select=False)


import time
import datetime
import sys

token = ''
with open('token.txt') as tok_file:
    token = tokefile.read()

session = Session(server_token=token)
client = UberRidesClient(session)

ts = time.time() - 14400
params = []

with open('Manhattan_Coordinates.csv', 'r') as f:
	points = csv.reader(f, delimiter=',')
	next(points, None)
	pa = []
	pb = []
	parama = []
	paramb = []
	i = 0
	for point in points:
		if i < 500:
			pa.append((point[0], point[1]))
		else:
			pb.append((point[0], point[1]))
		i += 1
	for point in pa:
		param = (
		    ('start_latitude', point[0]),
		    ('start_longitude', point[1]),
		    ('end_latitude', point[0]),
		    ('end_longitude', point[1]),
		)
		parama.append(param)
	for point in pb:
		param = (
		    ('start_latitude', point[0]),
		    ('start_longitude', point[1]),
		    ('end_latitude', point[0]),
		    ('end_longitude', point[1]),
		)
		paramb.append(param)


headers = {
    'Authorization': 'Token ' + token,
    'Accept-Language': 'en_US',
    'Content-Type': 'application/json',
}


rsa = (grequests.get('https://api.uber.com/v1.2/estimates/price', headers=headers, params=x) for x in parama)
low_estimates_a = [x.json()['prices'][1]['low_estimate'] for x in grequests.map(rsa)]
rsb = (grequests.get('https://api.uber.com/v1.2/estimates/price', headers=headers, params=x) for x in paramb)
low_estimates_b = [x.json()['prices'][1]['low_estimate'] for x in grequests.map(rsb)]

time_stamp = [datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')]

low_estimates = time_stamp + low_estimates_a + low_estimates_b
sys.stdout.write(",".join(map(str, low_estimates)) + '\n')

