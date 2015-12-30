#!/usr/bin/env python

# Loads JSON data from:
# https://atlas.ripe.net/measurements/3196765/
#
# Iterate results to filter out errors

import json
import urllib
import OpenSSL

# URL of measurement to examine
url = "https://atlas.ripe.net/api/v2/measurements/3196765/results?start=1451433600&stop=1451519999&format=json"

# Pull in the data from the server
response = urllib.urlopen(url)

# Load the JSON
data = json.loads(response.read())


for index in range(len(data)):        # Iterate thru results
  if data[index].has_key("dst_addr"):   # If result has a dst_addr
    print data[index]["dst_addr"]
    if data[index].has_key("cert"):     # If result has a cert
      for certindex in range(len(data[index]["cert"])):   # iterate thru certs
        # print cert components
        cert = data[index]["cert"][certindex]
        x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
        print x509.get_subject().get_components()
