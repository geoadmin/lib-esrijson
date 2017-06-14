from esrijson.base import EsriJSON
from esrijson.mapping import to_mapping


class Geometry(EsriJSON):

    def __init__(self, geometry=None, wkid=None, **extra):
        super(Geometry, self).__init__(**extra)
        self['geometry'] = self.to_instance(to_mapping(geometry), wkid)
