from esrijson.utils import orient_polygon_coords


class EsriJSON(dict):

    def __init__(self, **extra):
        self.update(extra)

    @classmethod
    def to_instance(cls, obj, wkid):
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
