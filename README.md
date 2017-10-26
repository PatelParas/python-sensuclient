python-sensuclient
==================

A barebones Python API client for [Sensu](https://github.com/sensu/sensu), a monitoring framework.

Installation
------------

```bash
pip install git+git://github.com/PatelParas/python-sensuclient
```

Sample Usage
------------
### Use it into your python class or builder helper class
```python
from sensuclient import Client
import json
sensu = Client('http://sensuAPIServer:4567')

# Get Client list  returntype:json
parsed = sensu.clients.list()
print json.dumps(parsed, indent=4, sort_keys=True)

# Get particular client returntype:json
parsed = sensu.clients.get("SensuClientName")
print json.dumps(parsed, indent=4, sort_keys=True)

# Get list of checks returntype:json
parsed = sensu.checks.list()
print json.dumps(parsed, indent=4, sort_keys=True)

# get Silenced entry list returntype:json
parsed = sensu.silences.list()
print json.dumps(parsed, indent=4, sort_keys=True)

# Do silence by sileceBySubscription name and expire time in seconds return HTTP 201
parsed = sensu.silences.sileceBySubscription("SensuSubscriptionName", 180)
print parsed.status_code
# Do silence by client  name and expire time in seconds return HTTP 201
parsed = sensu.silences.silenceByClientName("SensuClientName", 180)
print parsed.status_code

# Clear silence entry by Subscription name return HTTP 200, if entry not available HTTP 404
parsed = sensu.silences.clearBySubscription("SensuSubscriptionName")
print parsed.status_code
# Clear silence entry by Client name return HTTP 200, if entry not available HTTP 404
parsed = sensu.silences.clearByClientName("SensuClientName  ")
print parsed.status_code
```
### Inside python runtime
```python
>>> from sensuclient import Client
>>> sensu = Client('http://localhost:4567')
>>> sensu.clients.list()
[{u'address': u'127.0.0.1',
  u'name': u'localhost',
  u'subscriptions': [u'webservers'],
  u'timestamp': 1367704243},
 {u'address': u'127.0.0.2',
  u'name': u'example.com',
  u'subscriptions': [u'test'],
  u'timestamp': 1367704247},
  ...
  ]
```
