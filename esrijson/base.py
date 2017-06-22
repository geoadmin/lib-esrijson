import esrijson
from esrijson.utils import orient_polygon_coords


ESRI_GEOMETRY_KEYS = ['x', 'xmin', 'points', 'paths', 'rings']


def _is_geo_interface(obj):
    return 'type' in obj and 'coordinates' in obj


class EsriJSON(dict):

    def __init__(self, **extra):
        ## IMPORTANT USE GEOMETRYTYPE
        print 'init base'
        self["type"] = getattr(self, "type", type(self).__name__)
        self.update(extra)

    def __getattr__(self, name):
        """
        Permit dictionary items to be retrieved like object attributes

        :param name: attribute name
        :type name: str, int
        :return: dictionary value
        """
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        """
        Permit dictionary items to be set like object attributes.

        :param name: key of item to be set
        :type name: str
        :param value: value to set item to
        """

        self[name] = value

    def __delattr__(self, name):
        """
        Permit dictionary items to be deleted like object attributes

        :param name: key of item to be deleted
        :type name: str
        """

        del self[name]

    @classmethod
    def to_instance(cls, obj, wkid=None):
        print 'to instance'
        print type(obj)
        print '--------------------'
        # obj can be an OGC geometry or an instance of EsriJSON
        if isinstance(obj, EsriJSON):
            print 'instance of esrijson'
            print obj
            instance = obj
        elif isinstance(obj, dict):
            #import sys
            #sys.exit(0)
            d = {}
            for k in obj:
                d[k] = obj[k]
            #else:
            #    print d
            #    type_ = getattr(cls, 'type')
            #    factory = getattr(esrijson.factory, type_)
            #    return factory(**d)
            if any(k in ESRI_GEOMETRY_KEYS for k in obj):
                factory = getattr(esrijson.factory, 'Geometry')
                instance = factory(geometry=d)
            elif 'type' in d and d['type'] == 'Feature':
                factory = getattr(esrijson.factory, 'Feature')
                instance = factory(**d)
            else:
                instance = obj
        print 'some instance'
        print type(instance)
        print instance
        return instance
