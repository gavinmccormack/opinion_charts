""" Communicate with the coindesk API to retrieve prices """
import requests
import json
from datetime import datetime
from dateutil.parser import *


# Delete me
def p_json(json_t):
	out = json.dumps(json_t, indent=4, sort_keys=True)
	print(out)

class BitcoinPrices:
	def __init__(self):
		self.get_current_price()
		pass


	def check_connection(self):
		""" Returns false if API is not responding """
		response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
		if response.status_code != 200:
			return False
		return True

	def get_current_price(self,ticker='GBP'):
		""" Get current price in GBP, USD, or EUR """
		response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
		json = response.json()
		price = json['bpi'][ticker]['rate']
		return price

	def get_price_in_range(self, start_date, end_date, ticker='GBP'):
		""" Return bitcoin date : price dict over a timeframe """
		def convert_time_to_url_format(date):
			date = parse(date)
			date = date.strftime('%Y-%m-%d')
			print(date)
			return date
		try:
			start_date = convert_time_to_url_format(start_date)
			end_date = convert_time_to_url_format(end_date)
		except Exception as e:
			print(e)
			return "Unable to parse the start and end dates"
		endpoint = 'https://api.coindesk.com/v1/bpi/historical/close.json'
		endpoint = endpoint + "?start=" + start_date + "&end=" + end_date + "&currency=" + ticker
		response = requests.get(endpoint)
		json = response.json()
		p_json(json['bpi']) # Let's see what we get
		return json['bpi']


bp = BitcoinPrices()
bp.get_price_in_range("Tue Sep 1 23:59:11 2013","Tue Sep 5 23:59:11 2013")