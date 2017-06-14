import unittest
from esrijson import Geometry
from shapely import geometry


class TestGeometry(unittest.TestCase):

    def test_point(self):
        point = geometry.Point([0, 1])

        esri_spec = Geometry(geometry=point)
        self.assertEqual(esri_spec['geometry']['x'], 0)
        self.assertEqual(esri_spec['geometry']['y'], 1)
        self.assertNotIn('spatialReference', esri_spec['geometry'])

        esri_spec = Geometry(geometry=point, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'], 2056)

    def test_multipoint(self):
        multipoint = geometry.MultiPoint([[0, 1], [1, 2]])

        esri_spec = Geometry(geometry=multipoint)
        self.assertEqual(len(esri_spec['geometry']['points']), 2)
        self.assertEqual(esri_spec['geometry']['points'][0][0], 0)
        self.assertEqual(esri_spec['geometry']['points'][0][1], 1)
        self.assertEqual(esri_spec['geometry']['points'][1][0], 1)
        self.assertEqual(esri_spec['geometry']['points'][1][1], 2)
        self.assertNotIn('spatialReference', esri_spec['geometry'])

        esri_spec = Geometry(geometry=multipoint, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'], 2056)

    def test_linestring(self):
        linestring = geometry.LineString([(0, 0), (1, 1)])

        esri_spec = Geometry(geometry=linestring)
        self.assertEqual(len(esri_spec['geometry']['paths']), 1)
        self.assertEqual(len(esri_spec['geometry']['paths'][0]), 2)
        self.assertEqual(len(esri_spec['geometry']['paths'][0][0]), 2)
        self.assertEqual(esri_spec['geometry']['paths'][0][0][0], 0)
        self.assertEqual(esri_spec['geometry']['paths'][0][0][1], 0)
        self.assertEqual(esri_spec['geometry']['paths'][0][1][0], 1)
        self.assertEqual(esri_spec['geometry']['paths'][0][1][1], 1)
        self.assertNotIn('spatialReference', esri_spec['geometry'])

        esri_spec = Geometry(geometry=linestring, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'], 2056)

    def test_multilinestring(self):
        multilinestring = geometry.MultiLineString(
            [((0, 0), (1, 1)), ((-1, 0), (1, 0))])

        esri_spec = Geometry(geometry=multilinestring)
        self.assertEqual(len(esri_spec['geometry']['paths']), 2)
        self.assertEqual(len(esri_spec['geometry']['paths'][0]), 2)
        self.assertEqual(len(esri_spec['geometry']['paths'][0][0]), 2)
        self.assertEqual(esri_spec['geometry']['paths'][0][0][0], 0)
        self.assertEqual(esri_spec['geometry']['paths'][0][0][1], 0)
        self.assertEqual(esri_spec['geometry']['paths'][0][1][0], 1)
        self.assertEqual(esri_spec['geometry']['paths'][0][1][1], 1)
        self.assertEqual(esri_spec['geometry']['paths'][1][0][0], -1)
        self.assertEqual(esri_spec['geometry']['paths'][1][0][1], 0)
        self.assertEqual(esri_spec['geometry']['paths'][1][1][0], 1)
        self.assertEqual(esri_spec['geometry']['paths'][1][1][1], 0)
        self.assertNotIn('spatialReference', esri_spec['geometry'])

        esri_spec = Geometry(geometry=multilinestring, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'], 2056)

    def test_polygon(self):
        # Coordinates are oriented clock-wise
        polygon = geometry.Polygon([(0, 0), (1, 1), (2, 1), (0, 0)])

        esri_spec = Geometry(geometry=polygon)
        self.assertEqual(len(esri_spec['geometry']['rings']), 1)
        self.assertEqual(len(esri_spec['geometry']['rings'][0]), 4)
        self.assertEqual(len(esri_spec['geometry']['rings'][0][0]), 2)
        self.assertEqual(esri_spec['geometry']['rings'][0][0][0], 0)
        self.assertEqual(esri_spec['geometry']['rings'][0][0][1], 0)
        self.assertEqual(esri_spec['geometry']['rings'][0][1][0], 1)
        self.assertEqual(esri_spec['geometry']['rings'][0][1][1], 1)
        self.assertEqual(esri_spec['geometry']['rings'][0][2][0], 2)
        self.assertEqual(esri_spec['geometry']['rings'][0][2][1], 1)
        self.assertEqual(esri_spec['geometry']['rings'][0][3][0], 0)
        self.assertEqual(esri_spec['geometry']['rings'][0][3][1], 0)
        self.assertNotIn('spatialReference', esri_spec['geometry'])

        esri_spec = Geometry(geometry=polygon, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'], 2056)

    def test_multipolygon(self):
        polygons = [geometry.Polygon([(0, 0), (1, 1), (2, 1), (0, 0)]),
                    geometry.Polygon([(3, 3), (4, 4), (5, 3), (3, 3)])]
        multipolygon = geometry.MultiPolygon(polygons)
        esri_spec = Geometry(geometry=multipolygon)
        self.assertEqual(len(esri_spec['geometry']['rings']), 2)
