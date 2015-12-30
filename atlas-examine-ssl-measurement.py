#!/usr/bin/env python

# Loads JSON data from:
# https://atlas.ripe.net/measurements/3196765/
#
# Iterate results to filter out errors

if __name__ == "__main__":
  import json
  import urllib
  import OpenSSL
  import sys

  if len(sys.argv) > 1:
    # URL of measurement to examine
    url = sys.argv[1]
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
            print "", certindex
            cert = data[index]["cert"][certindex]
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
            print "  CertData: ", x509.get_subject().get_components()
            print "  SHA1:     ", x509.digest("sha1")
            print "  SHA256:   ", x509.digest("sha256")
  else:
    print "Usage:"
    print "", sys.argv[0], "<URL>"
    print "", "", "Where URL is an atlas ripe results api endpoint"
