from esrijson.base import EsriJSON
from esrijson.mapping import to_mapping
from shapely.geometry import Point, MultiPoint, LineString
from shapely.geometry import MultiLineString, Polygon, MultiPolygon


def create_point(geometry):
    if 'z' in geometry:
        return Point(geometry['x'], geometry['y'], geometry['z'])
    return Point(geometry['x'], geometry['y'])


def create_multipoint(geometry):
    return MultiPoint(geometry['points'])


def create_linestring(geometry):
    return LineString(geometry['paths'][0])


def create_multilinestring(geometry):
    return MultiLineString(geometry['paths'])


def create_polygon(geometry):
    return Polygon(geometry['rings'][0])


def create_multipolygon(geometry):
    rings = []
    for poly in geometry['rings']:
        exterior = None
        interiors = []
        p = Polygon(poly)
        if p.exterior.is_ccw:
            interiors.append(poly)
        else:
            exterior = p.exterior
        if exterior is None:
            raise ValueError(
                'Valid polygon types must at least define one exterior')
        rings.append(Polygon(shell=exterior, holes=interiors))
    return MultiPolygon(rings)


def to_shape(obj):
    geometry = obj['geometry'] if 'geometry' in obj else obj
    if 'x' in geometry:
        return create_point(geometry)
    elif 'points' in geometry:
        return create_multipoint(geometry)
    elif 'paths' in geometry and len(geometry['paths']) == 1:
        return create_linestring(geometry)
    elif 'paths' in geometry and len(geometry['paths']) > 1:
        return create_multilinestring(geometry)
    elif 'rings' in geometry and len(geometry['rings']) == 1:
        return create_polygon(geometry)
    elif 'rings' in geometry and len(geometry['rings']) > 1:
        return create_multipolygon(geometry)
    else:
        raise TypeError(
            'Esri geometry spec is incorrect or not supported')


class Geometry(EsriJSON):

    def __init__(self, geometry=None, wkid=None, **extra):
        super(Geometry, self).__init__(**extra)
        self['geometry'] = self.to_instance(to_mapping(geometry), wkid)
