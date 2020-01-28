from pprint import pprint
import argparse
import json

from geojson import FeatureCollection
import utm


def parser() -> dict:
	"""Argument parser function.
	
	Returns
	-------
	args : dict
		A dictionary containing the console arguments.
	"""

	ap = argparse.ArgumentParser()
	ap.add_argument("-f", "--filename", type=str,
					default="utm_format.geojson",
					help="Path to geojson file to be conveerted.")
	args = vars(ap.parse_args())

	return args


def validate_geojson(filename : str) -> bool:
	"""Function to validate if the input is a geojson file.
	
	Parameters
	----------
	filename : str
		The path to a geojson file.
	
	Returns
	-------
	bool
		A True/False validation of the extension.
	"""

	return filename.endswith('.geojson')


def read_geojson(filename : str) -> FeatureCollection:
	"""Function to load a geojson file as a FeatureCollection object.
	
	Parameters
	----------
	filename : str
		The path to a geojson file.
	
	Returns
	-------
	feature_collection : FeatureCollection
		A FeatureCollection object containing the geojson data.
	"""

	if validate_geojson(filename):
		with open(filename) as data_file:
			data = json.load(data_file)

		feature_collection = FeatureCollection(data)

		return feature_collection
	
	else:
		raise ValueError("Error with the file extension.")


def utm_to_latlong(f_collection : FeatureCollection) -> None:
	"""Function to update into the converted the coordinates of a 
	FeatureCollection object from UTM-WGS84 to standard latitude and
	longitude format.
	
	Parameters
	----------
	f_collection : FeatureCollection
		The FeatureColleciton object to be updated into the converted format.
	"""

	for feature in f_collection['features']:
		utm_format = feature['geometry']['coordinates']
		lat_long =  utm.to_latlon(utm_format[0], utm_format[1], 14, 'U')
		feature['geometry']['coordinates'] = list(lat_long)

	return


def save_geojson(f_collection : FeatureCollection, filename : str) -> None:
	"""Function to load a geojson file as a FeatureCollection object.
	
	Parameters
	----------
	filename : str
		The path to a geojson file.
	
	Returns
	-------
	feature_collection : FeatureCollection
		A FeatureCollection object containing the geojson data.
	"""

	if not validate_geojson(filename):
		filename += '.geojson'

	with open(filename, 'w') as data_file:
		json.dump(f_collection, data_file, indent=4)

	return


if __name__ == "__main__":
	# Read parameters from console:
	args = parser()
	filename = args['filename']

	# Load geojson object:
	geojson_object = read_geojson(filename)
	
	# Convert from UTM-WGS84 too (lat, long):
	utm_to_latlong(geojson_object)

	# Export converted object:
	save_geojson(geojson_object, 'centroides_manzanas_converted')	
	