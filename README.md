python-sensuclient
==================

A barebones Python API client for [Sensu](https://github.com/sensu/sensu), a monitoring framework.

Installation
------------

```bash
pip install git+git://github.com/cjlarose/python-sensuclient.git
```

Sample Usage
------------

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
