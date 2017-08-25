#!/usr/bin/env python

import csv
from geopy.geocoders import GoogleV3
import sys

geolocator = GoogleV3(api_key='AIzaSyDNKrEFWCsNtS0i-xX2BQpsRo1OlILFhBo', timeout=10) # AIzaSyDNKrEFWCsNtS0i-xX2BQpsRo1OlILFhBo

with open('wfm.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        #print row[0], row[3]
        #lines = row[1].splitlines()
        print >> sys.stderr, row[0]
        
        location = geolocator.geocode(" ".join([str(row[0]), str(row[3])]))

        if location:
            print "|".join([location.address, str(location.latitude), str(location.longitude)])
        else:
            print "ERR ", " ".join(lines[0:2])
        

