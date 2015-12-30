# atlas-tools-misc

misc tools that use data from RIPE atlas

## tools and usage

*	SSL Measurement
*	Traceroute data visualization (coming soon)
*	Maxmind and cymruwhois data integration (coming soon)

### Traceroute Measurement

`atlas-examine-traceroute-measurement.py` lets you examine a traceroute measurement in detail, printing out the ASN name, IPs and RTTs as returned by the probe.

#### Usage

```
python atlas-examine-traceroute-measurement.py "https://atlas.ripe.net/api/v2/measurements/3200170/results?start=1451433600&stop=1451519999&format=json"
```

#### Sample Output

```
From: 31.172.112.66
Probe ID: 11285
Proto: ICMP
0 31.172.112.65: 1.163 ms (255) 31.172.112.65: 0.795 ms (255) 31.172.112.65: 0.832 ms (255)  AS60955 Wavecon GmbH 
1 185.22.223.29: 0.393 ms (254) 185.22.223.29: 0.399 ms (254) 185.22.223.29: 0.359 ms (254)  AS60955 Wavecon GmbH 
2 185.22.223.81: 0.664 ms (253) 185.22.223.81: 0.62 ms (253) 185.22.223.81: 0.641 ms (253)  AS60955 Wavecon GmbH 
3 80.255.15.205: 0.677 ms (252) 80.255.15.205: 0.649 ms (252) 80.255.15.205: 0.69 ms (252)  AS201011 AS33891 Netzbetrieb GmbH 
4 80.255.15.22: 3.88 ms (250) 80.255.15.22: 3.838 ms (250) 80.255.15.22: 3.889 ms (250)  AS201011 AS33891 Netzbetrieb GmbH 
5 80.81.192.227: 25.969 ms (250) 80.81.192.227: 25.772 ms (250) 80.81.192.227: 25.773 ms (250)  AS12693 e.discom Telekommunikation GmbH 
6 193.111.37.114: 35.548 ms (58) 193.111.37.114: 35.526 ms (58) 193.111.37.114: 35.482 ms (58)  AS24724 ATM S.A. 
7 95.143.240.17: 36.899 ms (248) 95.143.240.17: 36.907 ms (248) 95.143.240.17: 36.909 ms (248)  AS49888 Ultranet Sp. z o.o. 
8 193.111.37.114: 35.668 ms (58) 193.111.37.114: 35.489 ms (58) 193.111.37.114: 35.557 ms (58)  AS24724 ATM S.A. 

From: 91.184.33.57
Probe ID: 1238
Proto: ICMP
0 91.184.32.1: 1.74 ms (64) 91.184.32.1: 1.498 ms (64) 91.184.32.1: 1.458 ms (64)  AS34225 SpeedPartner GmbH 
1 213.248.68.129: 1.45 ms (254) 213.248.68.129: 1.83 ms (254) 213.248.68.129: 1.455 ms (254)  AS1299 TeliaSonera AB 
2 62.115.115.47: 7.107 ms (253) 62.115.115.47: 7.055 ms (253) 62.115.115.47: 7.094 ms (253)  AS1299 TeliaSonera AB 
3 80.91.249.201: 7.077 ms (252) 80.91.249.201: 7.109 ms (252) 80.91.249.201: 7.059 ms (252)  AS1299 TeliaSonera AB 
4 213.248.103.62: 22.87 ms (250) 213.248.103.62: 25.898 ms (250) 213.248.103.62: 22.91 ms (250)  AS1299 TeliaSonera AB 
5 194.204.175.210: 25.874 ms (249) 194.204.175.210: 25.021 ms (249) 194.204.175.210: 25.099 ms (249)  AS5617 Orange Polska Spolka Akcyjna 
6 195.117.218.46: 25.061 ms (58) 195.117.218.46: 25.504 ms (58) 195.117.218.46: 25.116 ms (58)  AS5617 Orange Polska Spolka Akcyjna 
7 95.143.240.17: 25.765 ms (248) 95.143.240.17: 25.636 ms (248) 95.143.240.17: 25.606 ms (248)  AS49888 Ultranet Sp. z o.o. 
8 195.117.218.46: 25.124 ms (58) 195.117.218.46: 25.223 ms (58) 195.117.218.46: 25.326 ms (58)  AS5617 Orange Polska Spolka Akcyjna 

From: 185.6.78.96
Probe ID: 12993
Proto: ICMP
0 10.42.253.249: 0.493 ms (64) 10.42.253.249: 0.373 ms (64) 10.42.253.249: 0.365 ms (64)  None 
1 185.6.77.25: 0.748 ms (63) 185.6.77.25: 0.711 ms (63) 185.6.77.25: 0.693 ms (63)  AS202042 Skroutz Internet Services S.A. 
2 149.11.120.49: 1.623 ms (253) 149.11.120.49: 1.246 ms (253) 149.11.120.49: 1.337 ms (253)  AS174 Cogent Communications 
3 154.54.36.65: 1.912 ms (251) 154.54.36.65: 1.624 ms (251) 154.54.36.65: 1.687 ms (251)  AS174 Cogent Communications 
4 154.54.36.53: 13.254 ms (251) 154.54.36.53: 13.014 ms (251) 154.54.36.53: 13.245 ms (251)  AS174 Cogent Communications 
5 130.117.51.70: 22.671 ms (250) 130.117.51.70: 22.342 ms (250) 130.117.51.70: 22.383 ms (250)  AS174 Cogent Communications 
6 130.117.1.37: 29.414 ms (248) 130.117.1.37: 29.103 ms (248) 130.117.1.37: 29.177 ms (248)  AS174 Cogent Communications 
7 154.54.60.246: 41.613 ms (248) 154.54.60.246: 41.293 ms (248) 154.54.60.246: 41.492 ms (248)  AS174 Cogent Communications 
8 149.6.70.50: 42.265 ms (247) 149.6.70.50: 41.653 ms (247) 149.6.70.50: 41.857 ms (247)  AS174 Cogent Communications 
9 83.238.250.129: 55.319 ms (239) 83.238.250.129: 53.657 ms (239) 83.238.250.129: 57.204 ms (239)  AS12741 Netia SA 
10 *: False ms (0) 87.204.226.101: 48.385 ms (54) 87.204.226.101: 48.174 ms (54)  AS12741 Netia SA 
11 87.204.226.167: 52.862 ms (53) 87.204.226.167: 52.649 ms (53) 87.204.226.167: 52.446 ms (53)  AS12741 Netia SA 
12 87.204.225.127: 53.053 ms (52) 87.204.225.127: 52.853 ms (52) 87.204.225.127: 52.756 ms (52)  AS12741 Netia SA 
13 62.87.244.18: 52.81 ms (51) 62.87.244.18: 52.775 ms (51) 62.87.244.18: 52.841 ms (51)  AS12741 Netia SA 
14 95.143.240.17: 52.938 ms (241) 95.143.240.17: 52.999 ms (241) 95.143.240.17: 52.976 ms (241)  AS49888 Ultranet Sp. z o.o. 
15 62.87.244.18: 52.869 ms (51) 62.87.244.18: 52.828 ms (51) 62.87.244.18: 52.843 ms (51)  AS12741 Netia SA 

<snip>
```

### SSL Measurement

`atlas-examine-ssl-measurement.py` lets you examine an SSL measurement in detail, printing out the `dst_addr` and details of the certificate chain as returned by the probe.

#### Usage

```
python atlas-examine-ssl-measurement.py https://atlas.ripe.net/api/v2/measurements/3198534/results?format=json
```

#### Sample Output

```
31.13.69.228
 0
  CertData:  [('C', 'US'), ('ST', 'CA'), ('L', 'Menlo Park'), ('O', 'Facebook, Inc.'), ('CN', '*.facebook.com')]
  SHA1:      86:7C:B2:93:94:87:87:8A:6E:4D:B2:52:36:AC:92:AA:76:F0:9D:E3
  SHA256:    0F:99:39:3D:53:18:AE:D8:48:B7:28:7E:5A:AC:FE:79:7C:C5:C5:71:FF:DF:F8:8C:B0:B8:D6:0B:30:4D:97:8F
 1
  CertData:  [('C', 'US'), ('O', 'DigiCert Inc'), ('OU', 'www.digicert.com'), ('CN', 'DigiCert High Assurance CA-3')]
  SHA1:      42:85:78:55:FB:0E:A4:3F:54:C9:91:1E:30:E7:79:1D:8C:E8:27:05
  SHA256:    21:EB:37:AB:4C:F6:EF:89:65:EC:17:66:40:9C:A7:6B:8B:2E:03:F2:D1:A3:88:DF:73:42:08:E8:6D:EE:E6:79
31.13.77.36
 0
  CertData:  [('C', 'US'), ('ST', 'CA'), ('L', 'Menlo Park'), ('O', 'Facebook, Inc.'), ('CN', '*.facebook.com')]
  SHA1:      86:7C:B2:93:94:87:87:8A:6E:4D:B2:52:36:AC:92:AA:76:F0:9D:E3
  SHA256:    0F:99:39:3D:53:18:AE:D8:48:B7:28:7E:5A:AC:FE:79:7C:C5:C5:71:FF:DF:F8:8C:B0:B8:D6:0B:30:4D:97:8F
 1
  CertData:  [('C', 'US'), ('O', 'DigiCert Inc'), ('OU', 'www.digicert.com'), ('CN', 'DigiCert High Assurance CA-3')]
  SHA1:      42:85:78:55:FB:0E:A4:3F:54:C9:91:1E:30:E7:79:1D:8C:E8:27:05
  SHA256:    21:EB:37:AB:4C:F6:EF:89:65:EC:17:66:40:9C:A7:6B:8B:2E:03:F2:D1:A3:88:DF:73:42:08:E8:6D:EE:E6:79
173.252.90.132
 0
  CertData:  [('C', 'US'), ('ST', 'CA'), ('L', 'Menlo Park'), ('O', 'Facebook, Inc.'), ('CN', '*.facebook.com')]
  SHA1:      86:7C:B2:93:94:87:87:8A:6E:4D:B2:52:36:AC:92:AA:76:F0:9D:E3
  SHA256:    0F:99:39:3D:53:18:AE:D8:48:B7:28:7E:5A:AC:FE:79:7C:C5:C5:71:FF:DF:F8:8C:B0:B8:D6:0B:30:4D:97:8F
 1
  CertData:  [('C', 'US'), ('O', 'DigiCert Inc'), ('OU', 'www.digicert.com'), ('CN', 'DigiCert High Assurance CA-3')]
  SHA1:      42:85:78:55:FB:0E:A4:3F:54:C9:91:1E:30:E7:79:1D:8C:E8:27:05
  SHA256:    21:EB:37:AB:4C:F6:EF:89:65:EC:17:66:40:9C:A7:6B:8B:2E:03:F2:D1:A3:88:DF:73:42:08:E8:6D:EE:E6:79
173.252.74.68
 0
  CertData:  [('C', 'US'), ('ST', 'CA'), ('L', 'Menlo Park'), ('O', 'Facebook, Inc.'), ('CN', '*.facebook.com')]
  SHA1:      86:7C:B2:93:94:87:87:8A:6E:4D:B2:52:36:AC:92:AA:76:F0:9D:E3
  SHA256:    0F:99:39:3D:53:18:AE:D8:48:B7:28:7E:5A:AC:FE:79:7C:C5:C5:71:FF:DF:F8:8C:B0:B8:D6:0B:30:4D:97:8F
 1
  CertData:  [('C', 'US'), ('O', 'DigiCert Inc'), ('OU', 'www.digicert.com'), ('CN', 'DigiCert High Assurance CA-3')]
  SHA1:      42:85:78:55:FB:0E:A4:3F:54:C9:91:1E:30:E7:79:1D:8C:E8:27:05
  SHA256:    21:EB:37:AB:4C:F6:EF:89:65:EC:17:66:40:9C:A7:6B:8B:2E:03:F2:D1:A3:88:DF:73:42:08:E8:6D:EE:E6:79
<snip>
```
