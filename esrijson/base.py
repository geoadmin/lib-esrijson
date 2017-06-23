from __future__ import unicode_literals

import esrijson


ESRI_GEOMETRY_KEYS = ['x', 'xmin', 'points', 'paths', 'rings']


class EsriJSON(dict):

    def __init__(self, **extra):
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
    def to_instance(cls, obj, default=None, wkid=None):
        # for dumps, alternate default
        if obj is None and default is not None:
            instance = default()
        elif isinstance(obj, EsriJSON):
            instance = obj
        elif isinstance(obj, dict):
            d = {}
            for k in obj:
                d[k] = obj[k]
            if any(k in ESRI_GEOMETRY_KEYS for k in obj):
                factory = getattr(esrijson.factory, 'Geometry')
                instance = factory(geometry=d)
            elif 'attributes' in d and 'geometry' in d:
                factory = getattr(esrijson.factory, 'Feature')
                instance = factory(**d)
            else:
                instance = obj
        return instance
