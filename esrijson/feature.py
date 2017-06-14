from .base import EsriJSON
from .geometry import Geometry


class Feature(EsriJSON):

    def __init__(self, id=None, attributes=None, geometry=None, wkid=None, extra**)

        """
        Initialises a Feature object with the given parameters.

        :param id: Feature identifier, such as a sequential number.
        :type id: str, int
        :param geometry: Geometry corresponding to the feature. (a shapely geomety)
        :param attributes: Dict containing the attributes of the feature.
        :type attributes: dict
        """
        super(Feature, self).__init__(**extra)
        if id is not None:
            self["id"] = id
        self['geometry'] = (self.to_instance(geometry)
                            if geometry else None)
        self['attributes'] = attributes or {}


    def to_instance(self, geometry):
        return
