import requests
import json
from sys import argv
from urllib.parse import quote_plus

class RestClient(object):

	def __init__(self, zws_id):
		self.zws_id = zws_id

	def generate_city_state_zip(self, city, state, zip_code):
		if(city != None and state != None and zip_code != None):
			encoded_string = quote_plus(",".join([city, " "+state, " "+zip_code]))
		elif(city != None and state != None and zip_code == None):
			encoded_string = quote_plus(",".join([city, " "+state]))
		elif(city != None and state == None and zip_code != None):
			encoded_string = quote_plus(",".join([city, " "+zip_code]))
		else:
			raise TypeError("None of the fields were entered. Need to enter valid fields.")
		return encoded_string

	def get_zestimate(self, z_pid, rent_zestimate):
		"""Function that uses zillow api to request 
		estimates on a specific property.

		Args:
			z_pid (str): The Zillow property id.
			rent_zestimate (bool): Indicate whether or not to return rent estimates
		
		Returns:
			The surface properties for which a zestimate exists.
		"""
		request_url = "http://www.zillow.com/webservice/GetZestimate.htm"
		parameters = {"zws-id": self.zws_id, "zpid": z_pid, "rentzestimate": rent_zestimate}
		print(requests.get(request_url, params=parameters))
		# response = requests.get(request_url, params=parameters).json()
		# except:
		# 	print("JSON was invalid: ", response_body)
		# return response_body

	def get_property_info(self, address, city, state, zip_code, rent_zestimate):
		"""Finds a property for a specified address

		Args:
			address (str): The street address of the property you wish to search for.
			city (str): The specific city used in search results.
			state (str): The two letter state identification code used in search results.
			zip_code (str): The zip_code used in search results.
			rent_zestimate (bool): Flag to return or not return rest estimate if available.

		Returns:
			Data the properties located at the specified address.
		"""
		request_url = "http://www.zillow.com/webservice/GetSearchResults.htm"
		parameters = {"zws-id": self.zws_id, "address": quote_plus(address), "citystatezip": self.generate_city_state_zip(city, state, zip_code), "rentzestimate": rent_zestimate}
		print(parameters)
		return requests.get(request_url, params=parameters).json()

if __name__ == '__main__':
	#testing string generation