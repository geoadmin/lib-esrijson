import esrijson
from shapely import geometry


feat = esrijson.Feature(geometry=geometry.Point(1, 4), attributes={'name': 'dummy', 'val': 1}, wkid=2056)

dumped = esrijson.dumps(feat)
loaded = esrijson.loads(dumped)
print(loaded)
print(type(loaded))

geom = esrijson.to_shape({"paths": [[[0.0, 0.0], [1.0, 1.0]], [[-1.0, 0.0], [1.0, 0.0]]]})
print(getattr(geom, '__geo_interface__'))


esri_geom = esrijson.from_shape(geom)
print(esri_geom)
