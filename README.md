# atlas-tools-misc

misc tools that use data from RIPE atlas

## tools and usage

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
