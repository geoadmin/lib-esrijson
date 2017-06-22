try:
    import simplejson as json
except ImportError:
    import json

import esrijson


GEO_INTERFACE_MARKER = '__geo_interface__'


# Returns a geo interface ogc dict or an esrijson dict or instance.
# Shapely objects have a geo interface attribute.
def to_mapping(obj):

    mapping = getattr(obj, GEO_INTERFACE_MARKER, None)

    if mapping is not None:
        return mapping

    if isinstance(obj, esrijson.base.EsriJSON):
        return obj

    return json.loads(json.dumps(obj))
