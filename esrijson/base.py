from shapely.geometry import Polygon
from shapely.geometry.polygon import orient


# For EsriJSON, exterior rings are oriented clockwise,
# while holes are oriented counter-clockwise.
# For GeoJSON, Polygons with multiple rings, the first must be the exterior
# ring and any others must be interior rings or holes.
def _orient_polygon_coords(coords):
    oriented_esri_coords = []
    for i in range(0, len(coords)):
        poly = Polygon(coords[i])
        # Orient the first poly clock-wise (exterior ring)
        if i == 0:
            c = list(orient(poly, sign=-1.0).exterior.coords)
        else:
            c = list(orient(poly).exterior.coords)
        oriented_esri_coords.append(c)
    return oriented_esri_coords


class EsriJSON(dict):

    def __init__(self, **extra):
        self.update(extra)

    @classmethod
    def to_instance(self, obj, wkid):
        # obj can be an OGC geometry or an instance of EsriJSON
        if isinstance(obj, EsriJSON):
            return dict(obj)['geometry']
        else:
            esri_geom = {}

            # We use __geo_interface__ from GDAL (shapely)
            type_ = obj.pop('type')
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
                    esri_geom['rings'] = _orient_polygon_coords(coords)
                    if len(coords[0][0]) == 3:
                        esri_geom['hasZ'] = True
                elif type_ == 'MultiPolygon':
                    esri_geom['rings'] = []
                    for poly in coords:
                        esri_geom['rings'].append(
                            _orient_polygon_coords(poly)[0])
                    if len(coords[0][0][0]) == 3:
                        esri_geom['hasZ'] = True
                else:
                    raise TypeError(
                        'OGC geometry type %s is not supported' % type_)
            if wkid:
                esri_geom['spatialReference'] = {'wkid': int(wkid)}
            return esri_geom
