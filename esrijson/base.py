

class EsriJSON(dict):

    def __init__(self, extra**):

        super(GeoJSON, self).__init__()

        self.update(extra)

    @classmethod
    def to_instance(cls, ob, default=None, strict=False):
        return ''
