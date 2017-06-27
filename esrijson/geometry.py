from esrijson.base import EsriJSON
from esrijson.utils import orient_polygon_coords
from shapely.geometry import Point, MultiPoint, LineString, box
from shapely.geometry import MultiLineString, Polygon, MultiPolygon


GEO_INTERFACE_MARKER = '__geo_interface__'


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


def _is_bbox(bbox):
    if type(bbox) == list and len(bbox) == 4:
        if bbox[0] > bbox[2] or bbox[1] > bbox[3]:
            raise ValueError(
                'Invalid bbox, must be [xmin, ymin, xmax, ymax]')
        return True


def to_shape(obj):
    geometry = obj['geometry'] if 'geometry' in obj else obj
    if 'x' in geometry:
        return create_point(geometry)
    elif 'xmin' in geometry or _is_bbox(geometry):
        if type(geometry) == list:
            return box(*geometry)
        else:
            return box(geometry['xmin'], geometry['ymin'],
                       geometry['xmax'], geometry['ymax'])
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


def from_shape(obj, wkid=None):
    obj = getattr(obj, GEO_INTERFACE_MARKER, None)
    if obj is None:
        return obj
    esri_geom = {}
    # We use __geo_interface__ from GDAL (shapely)
    type_ = obj.pop('type')
    if type_ == 'GeometryCollection':
        # No concept of GeometryCollection in esri_json therefore we take
        # the first one only
        if len(obj['geometries']) == 0:
            return esri_geom
        first = obj['geometries'][0]
        type_ = first.pop('type')
        coords = first.pop('coordinates')
    else:
        coords = obj.pop('coordinates')
    if type_:
        if type_ == 'Point':
            esri_geom['x'] = coords[0]
            esri_geom['y'] = coords[1]
            if len(coords) == 3:
                esri_geom['z'] = coords[2]
        elif type_ == 'MultiPoint':
            esri_geom['points'] = coords
            if len(coords[0]) == 3:
                esri_geom['hasZ'] = True
        elif type_ == 'LineString':
            esri_geom['paths'] = [coords]
            if len(coords[0]) == 3:
                esri_geom['hasZ'] = True
        elif type_ == 'MultiLineString':
            esri_geom['paths'] = coords
            if len(coords[0][0]) == 3:
                esri_geom['hasZ'] = True
        elif type_ == 'Polygon':
            esri_geom['rings'] = orient_polygon_coords(coords)
            if len(coords[0][0]) == 3:
                esri_geom['hasZ'] = True
        elif type_ == 'MultiPolygon':
            esri_geom['rings'] = []
            for poly in coords:
                esri_geom['rings'].append(
                    orient_polygon_coords(poly)[0])
            if len(coords[0][0][0]) == 3:
                esri_geom['hasZ'] = True
        else:
            raise TypeError(
                'OGC geometry type %s is not supported' % type_)
    if wkid:
        esri_geom['spatialReference'] = {'wkid': int(wkid)}
    return esri_geom


class Geometry(EsriJSON):

    def __init__(self, geometry=None, **extra):
        super(Geometry, self).__init__(**extra)
        if 'x' in geometry and 'y' in geometry:
            self['x'] = geometry['x']
            self['y'] = geometry['y']
            if 'z' in geometry:
                self['z'] = geometry['z']
        elif all(k in ['xmin', 'ymin', 'xmax', 'ymax'] for k in geometry):
            self['xmin'] = geometry['xmin']
            self['ymin'] = geometry['ymin']
            self['xmax'] = geometry['xmax']
            self['ymax'] = geometry['ymax']
            if 'zmin' in geometry and 'zmax' in geometry:
                self['zmin'] = geometry['zmin']
                self['zmax'] = geometry['zmax']
        elif 'points' in geometry:
            self['points'] = geometry['points']
        elif 'paths' in geometry:
            self['paths'] = geometry['paths']
        elif 'rings' in geometry:
            self['rings'] = geometry['rings']

        if 'hasZ' in geometry:
            self['hasZ'] = geometry['hasZ']

        if 'spatialReference' in geometry:
            self['spatialReference'] = geometry['spatialReference']
