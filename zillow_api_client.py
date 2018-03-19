import requests
from sys import argv
from urllib.parse import quote_plus

class RestClient(object):

	def __init__(self, zws_id):
		self.zws_id = zws_id

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
		data = requests.get(request_url, params=parameters).json()
		return data

	def get_property_info(self, address, city, state, zip_code, rent_zestimate):
		"""Finds a property for a specified address

		Args:
			address (str): The street address of the property you wish to search for.
			city_state_zip (str): Url encoded string that includes city+state and or zipcode.
			rent_zestimate (bool): Flag to return or not return rest estimate if available.

		Returns:
			Data the properties located at the specified address.
		"""
		request_url = "http://www.zillow.com/webservice/GetSearchResults.htm"
		parameters = {"zws-id": self.zws_id, "address": address, "citystatezip": zip_code, "rentzestimate": rent_zestimate}
		data = requests.get(request_url, params=parameters).json()
		return data

	def generate_city_state_zip(self, city, state, zip_code):
		if(city != None and state != None and zip_code != None):
			encoded_string = quote_plus(",".join([city, state, zip_code]))
		elif(city != None and state != None and zip_code == None):
			encoded_string = quote_plus(",".join([city, state]))
		elif(city != None and state == None and zip_code != None):
			encoded_string = quote_plus(",".join([city, zip_code]))
		else:
			raise TypeError("None of the fields were entered. Need to enter valid fields.")
		return encoded_string

if __name__ == '__main__':
	#testing string generation
	client = RestClient("X1-ZWz1gaiw11wnpn_7c2wf")
	print(client.generate_city_state_zip("lawrence", "MA", "01841"))