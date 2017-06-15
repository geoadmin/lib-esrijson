from esrijson.base import EsriJSON
from esrijson.mapping import to_mapping


class Feature(EsriJSON):

    def __init__(self, id=None, geometry=None, wkid=None, attributes=None,
                 **extra):

        """
        Initialises a Feature object with the given parameters.

        :param id: Feature identifier, such as a sequential number.
        :type id: str, int (not comp. in esri spec)
        :param geometry: Geometry corresponding to the feature.
        :param wkid: well-know ID of the spatial reference.
        :param attributes: Dict containing the attributes of the feature.
        :type attributes: dict
        """
        super(Feature, self).__init__(**extra)
        if id is not None:
            self["id"] = id
        if geometry:
            self['geometry'] = self.to_instance(to_mapping(geometry), wkid)
        else:
            self['geometry'] = None
        self['attributes'] = attributes or {}
