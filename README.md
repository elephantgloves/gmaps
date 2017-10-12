# gmaps
--------
Current state: minimal working version
Supports: Windows 7, python 2.7
Packages used: csv, json, os, sys

Outputs a bunch of google map images for list of x,y coordinates in CSV file for (very) quick viewing of x,y locations.
--------
config.json file holds below config settings:
API keys 
output map size, magnification, type (hybrid, satellite)

Please set as necessary.
--------
To run:
gmaps.py [sourceCSVfile.csv]

Replace with source CSV file holding x,y coordinates.
If CSV in same file as python file, can use relative path. Otherwise use absolute path.

By default outputs target html file into same directory as python file.


