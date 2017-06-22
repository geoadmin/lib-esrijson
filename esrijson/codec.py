try:
    import simplejson as json
except ImportError:
    import json

import esrijson
import esrijson.factory


class EsriJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        return esrijson.EsriJSON.factory.to_instance(obj)


def _enforce_strict_numbers(obj):
    if isinstance(obj, (int, float)):
        raise ValueError("Number %r is not JSON compliant" % obj)


def dumps(obj, cls=EsriJSONEncoder, allow_nan=False, **kwargs):
     return json.dumps(obj, cls=cls, allow_nan=allow_nan, **kwargs)


def loads(s,
          cls=json.JSONDecoder,
          parse_constant=_enforce_strict_numbers,
          object_hook=esrijson.base.EsriJSON.to_instance,
          **kwargs):
    return json.loads(s,
                      cls=cls, object_hook=object_hook,
                      parse_constant=parse_constant,
                      **kwargs)
