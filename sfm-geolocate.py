#!/usr/bin/env python

import codecs
import csv
import sys

from geopy.geocoders import GoogleV3

geolocator = GoogleV3(api_key='AIzaSyDNKrEFWCsNtS0i-xX2BQpsRo1OlILFhBo', timeout=10) # AIzaSyDNKrEFWCsNtS0i-xX2BQpsRo1OlILFhBo

with codecs.open('sfm.csv.clean',  encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        lines = row[1].splitlines()
        location = geolocator.geocode(" ".join(lines[0:2]))
        
        print >> sys.stderr, location.address
        if location:
            print "|".join([" ".join(lines[0:2]), str(location.latitude), str(location.longitude)])
        else:
            print "ERR ", " ".join(lines[0:2])
        

