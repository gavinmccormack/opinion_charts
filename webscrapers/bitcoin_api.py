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
		def convert_time_to_format(date, date_format='%Y-%m-%d'):
			""" Should parse most date formats. Defaults to YYYY-MM-DD """
			try:
				date = parse(date)
				date = date.strftime(date_format)
				return date
			except Exception as e:
				print(e)
				return "Unable to parse this date"
		
		start_date = convert_time_to_format(start_date)
		end_date = convert_time_to_format(end_date)
		endpoint = 'https://api.coindesk.com/v1/bpi/historical/close.json'
		endpoint = endpoint + "?start=" + start_date + "&end=" + end_date + "&currency=" + ticker
		response = requests.get(endpoint)
		json = response.json()

		# For the date formatting here, - is linux and # is windows. Which is a bit frustrating.
		price_data = {date: convert_time_to_format(date,'%a %b %#d %I:%M:%S %Y') for date, price in json['bpi'].items()}
		return price_data


