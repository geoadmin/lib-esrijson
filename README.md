esrijson
========

[![Build Status](https://travis-ci.org/geoadmin/esrijson.svg?branch=master)](https://travis-ci.org/geoadmin/esrijson)


Introduction
------------

This module is meant to build a bridge between GDAL `__geo_interface__` property via [Shapely](https://github.com/Toblerity/Shapely).
There is no concept of `GeometryCollection` in esrijson syntax, so there is currently no support for this.
This library is heavily inspired by [python-geojson](https://github.com/frewsxcv/python-geojson).

Usage
-----

```python
import esrijson
from shapely import geometry

# Create an esrijson feature
feat = esrijson.Feature(geometry=geometry.Point(1, 4), attributes={'name': 'dummy', 'val': 1}, wkid=2056)
# Dump to json
dumped = esrijson.dumps(feat)
# Load to Feature back again
loaded = esrijson.loads(dumped)
print(loaded)
print(type(loaded))

>>> {'geometry': {'y': 4.0, 'x': 1.0}, 'spatialReference': {u'wkid': 2056}},'attributes': {u'name': u'dummy', u'val': 1}}
>>> <class 'esrijson.feature.Feature'>

# You can also transform an esri json like object into a shapely object
geom = esrijson.to_shape({"paths": [[[0.0, 0.0], [1.0, 1.0]], [[-1.0, 0.0], [1.0, 0.0]]]})
print(getattr(geom, '__geo_interface__')

>>> {'type': 'MultiLineString', 'coordinates': (((0.0, 0.0), (1.0, 1.0)), ((-1.0, 0.0), (1.0, 0.0)))}

# And of your do the same operation back again
esri_geom = esrijson.from_shape(geom)
print(esri_geom)
>>> {'paths': (((0.0, 0.0), (1.0, 1.0)), ((-1.0, 0.0), (1.0, 0.0)))}
```
