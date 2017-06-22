import esrijson
from shapely import geometry


feat = esrijson.Feature(geometry=geometry.Point(1, 4), attributes={'name': 'dummy', 'val': 1})
#print(feat)
# With wkid
feat = esrijson.Feature(geometry=geometry.Point(1, 4), attributes={'name': 'dummy', 'val': 1})

es_d = esrijson.dumps(feat)
print 'esri'
es_l = esrijson.loads(es_d)
print es_l
print(type(es_l))
#print(es_d)
#print(type(es_l))
#print(es_d)
#
#import geojson
#print 'geo'
#geo = geojson.Feature(geometry=geometry.Point(1, 4), properties={'name': 'dummy', 'val': 1})
#ge_d = geojson.dumps(geo)
#ge_l = geojson.loads(ge_d)
#print(type(ge_d))
#print(ge_d)
#print(type(ge_l))
#print(ge_l)
