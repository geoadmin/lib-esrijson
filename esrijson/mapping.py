try:
    import simplejson as json
except ImportError:
    import json
import esrijson


def to_mapping(obj):

    if isinstance(obj, esrijson.base.EsriJSON):
        return obj

    return json.loads(json.dumps(obj))
