# UTM-WGS84 to standard (lat, long) converter 📍

This repo contains a quick script to convert a geojson file from UTM-WGS84 to standard (lat, long) format.


### Dependencies

You'll need to have Python 3.6+ installed on your system.

This script uses:
- [utm](https://github.com/Turbo87/utm)
- [geojson](https://github.com/jazzband/geojson)

To install dependencies using `pip`, simply run:

```bash
pip install -r requirements.txt
```

> NOTE: You can create a virtual environment or install the dependencies globally.


### Usage

The parser can print a quick help menu for you:

```bash
$ python converter.py -h
usage: converter.py [-h] [-f FILENAME] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -f FILENAME, --filename FILENAME
                        Path to geojson file to be converted.
  -o OUTPUT, --output OUTPUT
                        Name of the geojson output file after conversion.
```

To run the script:

```bash
$ python converter.py -f centroides_manzanas.geojson -o centroides_manzanas_converted.geojson
```


### License

This repo contains a MIT license.

