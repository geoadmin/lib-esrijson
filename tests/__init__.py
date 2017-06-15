import unittest
from esrijson import to_shape
from shapely import geometry


class BaseTestClass(unittest.TestCase):

    def getPoint(self, hasZ=False):
        if hasZ:
            return geometry.Point([0, 1, 5])
        return geometry.Point([0, 1])

    def getMultiPoint(self, hasZ=False):
        if hasZ:
            return geometry.MultiPoint([[0, 1, 5], [1, 2, 5]])
        return geometry.MultiPoint([[0, 1], [1, 2]])

    def getLineString(self, hasZ=False):
        if hasZ:
            return geometry.LineString([(0, 0, 5), (1, 1, 5)])
        return geometry.LineString([(0, 0), (1, 1)])

    def getMultiLineString(self, hasZ=False):
        if hasZ:
            return geometry.MultiLineString(
                [((0, 0, 5), (1, 1, 5)), ((-1, 0, 6), (1, 0, 6))])
        return geometry.MultiLineString(
            [((0, 0), (1, 1)), ((-1, 0), (1, 0))])

    def getPolygon(self, hasZ=False):
        if hasZ:
            return geometry.Polygon(
                [(0, 0, 5), (1, 1, 5), (2, 1, 5), (0, 0, 5)])
        return geometry.Polygon([(0, 0), (1, 1), (2, 1), (0, 0)])

    def getMultiPolygon(self, hasZ=False):
        if hasZ:
            return geometry.MultiPolygon(
                [geometry.Polygon(
                    [(0, 0, 5), (1, 1, 5), (2, 1, 5), (0, 0, 5)]),
                 geometry.Polygon(
                    [(3, 3, 5), (4, 4, 5), (5, 3, 5), (3, 3, 5)])])
        return geometry.MultiPolygon(
            [geometry.Polygon([(0, 0), (1, 1), (2, 1), (0, 0)]),
             geometry.Polygon([(3, 3), (4, 4), (5, 3), (3, 3)])])

    def getGeometryCollection(self):
        return geometry.collection.GeometryCollection([
            self.getPoint(),
            self.getMultiPoint(),
            self.getLineString(),
            self.getMultiLineString(),
            self.getPolygon(),
            self.getMultiPolygon()
        ])

    def assertSpatialReference(self, geometry, wkid):
        if wkid:
            self.assertEqual(
                geometry['spatialReference']['wkid'],
                2056)
        else:
            self.assertNotIn('spatialReference', geometry)

    def assertPoint(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(geometry['x'], 0)
        self.assertEqual(geometry['y'], 1)
        if hasZ:
            self.assertEqual(geometry['z'], 5)
        self.assertSpatialReference(geometry, wkid)

    def assertMultiPoint(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(len(geometry['points']), 2)
        self.assertEqual(geometry['points'][0][0], 0)
        self.assertEqual(geometry['points'][0][1], 1)
        self.assertEqual(geometry['points'][1][0], 1)
        self.assertEqual(geometry['points'][1][1], 2)
        if hasZ:
            self.assertEqual(len(geometry['points']), 2)
            self.assertEqual(geometry['points'][0][2], 5)
            self.assertEqual(geometry['points'][1][2], 5)
            self.assertEqual(geometry['hasZ'], True)
        else:
            self.assertEqual(len(geometry['points'][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertLineString(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(geometry['paths'][0][0][0], 0)
        self.assertEqual(geometry['paths'][0][0][1], 0)
        self.assertEqual(geometry['paths'][0][1][0], 1)
        self.assertEqual(geometry['paths'][0][1][1], 1)
        if hasZ:
            self.assertEqual(geometry['paths'][0][0][2], 5)
            self.assertEqual(geometry['paths'][0][1][2], 5)
            self.assertEqual(geometry['hasZ'], True)
        else:
            self.assertEqual(len(geometry['paths'][0][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertMultiLineString(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(len(geometry['paths']), 2)
        self.assertEqual(geometry['paths'][0][0][0], 0)
        self.assertEqual(geometry['paths'][0][0][1], 0)
        self.assertEqual(geometry['paths'][0][1][0], 1)
        self.assertEqual(geometry['paths'][0][1][1], 1)
        self.assertEqual(geometry['paths'][1][0][0], -1)
        self.assertEqual(geometry['paths'][1][0][1], 0)
        self.assertEqual(geometry['paths'][1][1][0], 1)
        self.assertEqual(geometry['paths'][1][1][1], 0)
        if hasZ:
            self.assertEqual(geometry['paths'][0][0][2], 5)
            self.assertEqual(geometry['paths'][0][1][2], 5)
            self.assertEqual(geometry['paths'][1][0][2], 6)
            self.assertEqual(geometry['paths'][1][1][2], 6)
            self.assertEqual(geometry['hasZ'], True)
        else:
            self.assertEqual(len(geometry['paths'][0][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertPolygon(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(len(geometry['rings']), 1)
        self.assertEqual(len(geometry['rings'][0]), 4)
        self.assertEqual(geometry['rings'][0][0][0], 0)
        self.assertEqual(geometry['rings'][0][0][1], 0)
        self.assertEqual(geometry['rings'][0][1][0], 1)
        self.assertEqual(geometry['rings'][0][1][1], 1)
        self.assertEqual(geometry['rings'][0][2][0], 2)
        self.assertEqual(geometry['rings'][0][2][1], 1)
        self.assertEqual(geometry['rings'][0][3][0], 0)
        self.assertEqual(geometry['rings'][0][3][1], 0)
        if hasZ:
            self.assertEqual(geometry['rings'][0][0][2], 5)
            self.assertEqual(geometry['rings'][0][1][2], 5)
            self.assertEqual(geometry['rings'][0][2][2], 5)
            self.assertEqual(geometry['rings'][0][3][2], 5)
            self.assertEqual(geometry['hasZ'], True)
        else:
            self.assertEqual(len(geometry['rings'][0][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertMultiPolygon(self, geometry, hasZ=False, wkid=None):
        self.assertEqual(len(geometry['rings']), 2)
        self.assertEqual(len(geometry['rings'][0]), 4)
        self.assertEqual(geometry['rings'][0][0][0], 0)
        self.assertEqual(geometry['rings'][0][0][1], 0)
        self.assertEqual(geometry['rings'][0][1][0], 1)
        self.assertEqual(geometry['rings'][0][1][1], 1)
        self.assertEqual(geometry['rings'][0][2][0], 2)
        self.assertEqual(geometry['rings'][0][2][1], 1)
        self.assertEqual(geometry['rings'][0][3][0], 0)
        self.assertEqual(geometry['rings'][0][3][1], 0)
        self.assertEqual(geometry['rings'][1][0][0], 3)
        self.assertEqual(geometry['rings'][1][0][1], 3)
        self.assertEqual(geometry['rings'][1][1][0], 4)
        self.assertEqual(geometry['rings'][1][1][1], 4)
        self.assertEqual(geometry['rings'][1][2][0], 5)
        self.assertEqual(geometry['rings'][1][2][1], 3)
        self.assertEqual(geometry['rings'][1][3][0], 3)
        self.assertEqual(geometry['rings'][1][3][1], 3)
        if hasZ:
            self.assertEqual(geometry['rings'][0][0][2], 5)
            self.assertEqual(geometry['rings'][0][1][2], 5)
            self.assertEqual(geometry['rings'][0][2][2], 5)
            self.assertEqual(geometry['rings'][0][3][2], 5)
            self.assertEqual(geometry['rings'][1][0][2], 5)
            self.assertEqual(geometry['rings'][1][1][2], 5)
            self.assertEqual(geometry['rings'][1][2][2], 5)
            self.assertEqual(geometry['rings'][1][3][2], 5)
        else:
            self.assertEqual(len(geometry['rings'][0][0]), 2)
        self.assertSpatialReference(geometry, wkid)

    def assertToShape(self, first_shp, esri_spec, esri_spec_copy):
        shp = to_shape(esri_spec)
        shp_copy = to_shape(esri_spec_copy)
        self.assertEqual(
            getattr(first_shp, '__geo_interface__'),
            getattr(shp, '__geo_interface__'))
        self.assertEqual(
            getattr(first_shp, '__geo_interface__'),
            getattr(shp_copy, '__geo_interface__'))
