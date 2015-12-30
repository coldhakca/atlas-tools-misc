#!/usr/bin/env python

# Loads JSON data from:
# https://atlas.ripe.net/measurements/3196765/
#
# Iterate results to filter out errors

import json
import urllib

url = "https://atlas.ripe.net/api/v2/measurements/3196765/results?start=1451433600&stop=1451519999&format=json"

response = urllib.urlopen(url)

data = json.loads(response.read())

for index in range(len(data)):
  if data[index].has_key("dst_addr"):
    print data[index]["dst_addr"]
