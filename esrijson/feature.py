from esrijson.base import EsriJSON
from esrijson.geometry import from_shape
from esrijson.mapping import to_mapping


class Feature(EsriJSON):

    type_ = 'Feature'

    def __init__(self, geometry=None, wkid=None, attributes=None, id=None,
                 **extra):

        """
        Initialises a Feature object with the given parameters.

        :param geometry: Geometry corresponding to the feature.
        :param wkid: well-know ID of the spatial reference.
        :param attributes: Dict containing the attributes of the feature.
        :type attributes: dict
        :param id: Feature identifier, such as a sequential number.
        :type id: str, int
        """
        print 'init feature'
        super(Feature, self).__init__(**extra)
        self["type"] = getattr(self, "type", type(self).__name__)
        if id is not None:
            self['id'] = id
        if hasattr(geometry, '__geo_interface__'):
            self['geometry'] = from_shape(geometry, wkid=wkid)
        elif geometry:
            self['geometry'] = self.to_instance(geometry)
        else:
            self['geometry'] = None
        print attributes
        print type(attributes)
        print 'xxxxxxxxxxxxxxxxxx'
        self['attributes'] = attributes or {}
