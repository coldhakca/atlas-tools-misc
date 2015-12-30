#!/usr/bin/env python

# Examine RIPE Atlas SSL Measurement Data
#
# Loads JSON data from URL specified on cmdline:
# Usage:
#  ./atlas-examine-ssl-measurement.py <URL>
#    Where URL is an atlas ripe results api endpoint

if __name__ == "__main__":
  import json
  import urllib
  import OpenSSL
  import sys
  import GeoIP
  from dns import resolver,reversename

  if len(sys.argv) > 1:

    gi = GeoIP.open("/usr/local/share/GeoIP/GeoIPASNum.dat",GeoIP.GEOIP_STANDARD)

    # URL of measurement to examine
    url = sys.argv[1]
    # Pull in the data from the server
    response = urllib.urlopen(url)
    # Load the JSON
    data = json.loads(response.read())

    for index in range(len(data)):        # Iterate thru results
      print "From:", data[index]["from"]
      print "Probe ID:", data[index]["prb_id"]
      print "Proto:", data[index]["proto"]

      for resultindex in range(len(data[index]["result"])):
        print "%d" % resultindex,
        for resultrttindex in range(len(data[index]["result"][resultindex]["result"])):
          #print data[index]["result"][resultindex]["result"][resultrttindex]
          from_val = "*"
          rtt_val = False
          ttl_val = False
          asn_val = False

          if data[index]["result"][resultindex]["result"][resultrttindex].has_key("from"):
            from_val = data[index]["result"][resultindex]["result"][resultrttindex]["from"]
            addr=reversename.from_address(from_val)
            asn_val = gi.name_by_addr(from_val)
          if data[index]["result"][resultindex]["result"][resultrttindex].has_key("rtt"):
            rtt_val = data[index]["result"][resultindex]["result"][resultrttindex]["rtt"]
          if data[index]["result"][resultindex]["result"][resultrttindex].has_key("ttl"):
            ttl_val = data[index]["result"][resultindex]["result"][resultrttindex]["ttl"]
          print "%s: %s ms (%d)" % (from_val, rtt_val, ttl_val),
        print "", asn_val, ""
      print ""
  else:
    print "Usage:"
    print "", sys.argv[0], "<URL>"
    print "", "", "Where URL is an atlas ripe results api endpoint"
