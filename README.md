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
Source:    106.39.68.36
Dest:      159.106.121.75
Probe ID:  23691
Type:      Traceroute
Proto:     TCP
0 192.168.1.1: 0.719 ms (64) 192.168.1.1: 0.612 ms (64) 192.168.1.1: 0.606 ms (64)  None 
1 *: False ms (0) *: False ms (0) *: False ms (0)  False 
2 *: False ms (0) *: False ms (0) *: False ms (0)  False 
3 *: False ms (0) *: False ms (0) *: False ms (0)  False 
4 *: False ms (0) *: False ms (0) *: False ms (0)  False 
5 *: False ms (0) *: False ms (0) *: False ms (0)  False 
6 *: False ms (0) *: False ms (0) *: False ms (0)  False 

Source:    114.253.203.86
Dest:      46.82.174.68
Probe ID:  23707
Type:      Traceroute
Proto:     TCP
0 192.168.1.1: 0.448 ms (64) 192.168.1.1: 0.393 ms (64) 192.168.1.1: 0.382 ms (64)  None 
1 *: False ms (0) *: False ms (0) *: False ms (0)  False 
2 *: False ms (0) *: False ms (0) *: False ms (0)  False 
3 124.65.57.209: 2.355 ms (252) 124.65.57.209: 1.629 ms (252) 124.65.57.209: 1.687 ms (252)  AS4808 CNCGROUP IP network China169 Beijing Province Network 
4 *: False ms (0) *: False ms (0) *: False ms (0)  False 
5 *: False ms (0) *: False ms (0) *: False ms (0)  False 
6 *: False ms (0) *: False ms (0) 192.168.1.1: False ms (64) 192.168.1.1: False ms (64) 192.168.1.1: False ms (64) 114.253.192.1: False ms (254) 114.253.192.1: False ms (254) 114.253.192.1: False ms (254) *: False ms (0)  False 
7 *: False ms (0) *: False ms (0) *: False ms (0)  False 
8 *: False ms (0) *: False ms (0) *: False ms (0)  False 
9 *: False ms (0) *: False ms (0) *: False ms (0)  False 

Source:    60.191.110.189
Dest:      159.106.121.75
Probe ID:  23857
Type:      Traceroute
Proto:     TCP
0 10.11.11.254: 1.444 ms (64) 10.11.11.254: 1.438 ms (64) 10.11.11.254: 1.43 ms (64)  None 
1 *: False ms (0) *: False ms (0) *: False ms (0)  False 
2 192.168.100.251: 2.064 ms (62) 192.168.100.251: 3.009 ms (62) 192.168.100.251: 1.755 ms (62)  None 
3 218.108.83.129: 3.362 ms (252) *: False ms (0) *: False ms (0)  False 
4 *: False ms (0) *: False ms (0) *: False ms (0)  False 
5 *: False ms (0) *: False ms (0) *: False ms (0)  False 
6 *: False ms (0) *: False ms (0) *: False ms (0)  False 
7 *: False ms (0) *: False ms (0) 10.11.11.254: False ms (64) 10.11.11.254: False ms (64) 10.11.11.254: False ms (64) *: False ms (0)  False 
8 *: False ms (0) *: False ms (0) *: False ms (0)  False 
9 *: False ms (0) *: False ms (0) *: False ms (0)  False 

Source:    59.45.74.63
Dest:      203.98.7.65
Probe ID:  23874
Type:      Traceroute
Proto:     TCP
0 192.168.1.253: 0.521 ms (64) 192.168.1.253: 0.451 ms (64) 192.168.1.253: 0.42 ms (64)  None 
1 *: False ms (0) *: False ms (0) *: False ms (0)  False 
2 *: False ms (0) *: False ms (0) *: False ms (0)  False 
3 *: False ms (0) *: False ms (0) *: False ms (0)  False 
4 *: False ms (0) *: False ms (0) *: False ms (0)  False 
5 *: False ms (0) *: False ms (0) *: False ms (0)  False 
6 *: False ms (0) *: False ms (0) *: False ms (0)  False 

Source:    58.100.3.186
Probe ID:  23959
Type:      Traceroute
Proto:     TCP
0 address not allowed
 False 

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
