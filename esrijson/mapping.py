# Stolen from
# https://github.com/frewsxcv/python-geojson/blob/master/geojson/mapping.py
try:
    import simplejson as json
except ImportError:
    import json
from esrijson import EsriJSON


GEO_INTERFACE_MARKER = '__geo_interface__'


"""
:param obj: An object representing a feature.
:type obj: dict | EsriJSON instance | shapely geometry
"""


def to_mapping(obj):

    mapping = getattr(obj, GEO_INTERFACE_MARKER, None)

    if mapping is not None:
        return mapping

    if isinstance(obj, EsriJSON):
        return obj

    return json.loads(json.dumps(obj))
