import unittest
from esrijson import Geometry, to_shape
from shapely import geometry


class TestGeometry(unittest.TestCase):

    def assertToShape(self, first_shp, esri_spec, esri_spec_copy):
        shp = to_shape(esri_spec)
        shp_copy = to_shape(esri_spec_copy)
        self.assertEqual(
            getattr(first_shp, '__geo_interface__'),
            getattr(shp, '__geo_interface__'))
        self.assertEqual(
            getattr(first_shp, '__geo_interface__'),
            getattr(shp_copy, '__geo_interface__'))

    def test_point(self):
        point = geometry.Point([0, 1])

        esri_spec = Geometry(geometry=point)
        self.assertEqual(esri_spec['geometry']['x'], 0)
        self.assertEqual(esri_spec['geometry']['y'], 1)
        self.assertNotIn('spatialReference', esri_spec['geometry'])

        point = geometry.Point([0, 1, 5])
        esri_spec = Geometry(geometry=point)
        self.assertEqual(esri_spec['geometry']['z'], 5)
        self.assertNotIn('hasZ', esri_spec['geometry'])

        esri_spec = Geometry(geometry=point, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'],
            2056)
        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertEqual(
            esri_spec_copy['geometry']['spatialReference']['wkid'],
            2056)
        self.assertToShape(point, esri_spec, esri_spec_copy)

    def test_multipoint(self):
        multipoint = geometry.MultiPoint([[0, 1], [1, 2]])

        esri_spec = Geometry(geometry=multipoint)
        self.assertEqual(len(esri_spec['geometry']['points']), 2)
        self.assertEqual(esri_spec['geometry']['points'][0][0], 0)
        self.assertEqual(esri_spec['geometry']['points'][0][1], 1)
        self.assertEqual(esri_spec['geometry']['points'][1][0], 1)
        self.assertEqual(esri_spec['geometry']['points'][1][1], 2)
        self.assertNotIn('spatialReference', esri_spec['geometry'])

        multipoint = geometry.MultiPoint([[0, 1, 5], [1, 2, 5]])
        esri_spec = Geometry(geometry=multipoint)
        self.assertEqual(len(esri_spec['geometry']['points']), 2)
        self.assertEqual(esri_spec['geometry']['points'][0][2], 5)
        self.assertEqual(esri_spec['geometry']['points'][1][2], 5)
        self.assertEqual(esri_spec['geometry']['hasZ'], True)

        esri_spec = Geometry(geometry=multipoint, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'],
            2056)
        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertEqual(
            esri_spec_copy['geometry']['spatialReference']['wkid'],
            2056)
        self.assertToShape(multipoint, esri_spec, esri_spec_copy)

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

        linestring = geometry.LineString([(0, 0, 5), (1, 1, 5)])
        esri_spec = Geometry(geometry=linestring)
        self.assertEqual(esri_spec['geometry']['paths'][0][0][2], 5)
        self.assertEqual(esri_spec['geometry']['paths'][0][1][2], 5)
        self.assertEqual(esri_spec['geometry']['hasZ'], True)

        esri_spec = Geometry(geometry=linestring, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'],
            2056)
        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertEqual(
            esri_spec_copy['geometry']['spatialReference']['wkid'],
            2056)
        self.assertToShape(linestring, esri_spec, esri_spec_copy)

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

        multilinestring = geometry.MultiLineString(
            [((0, 0, 5), (1, 1, 5)), ((-1, 0, 6), (1, 0, 6))])
        esri_spec = Geometry(geometry=multilinestring)
        self.assertEqual(esri_spec['geometry']['paths'][0][0][2], 5)
        self.assertEqual(esri_spec['geometry']['paths'][0][1][2], 5)
        self.assertEqual(esri_spec['geometry']['paths'][1][0][2], 6)
        self.assertEqual(esri_spec['geometry']['paths'][1][1][2], 6)
        self.assertEqual(esri_spec['geometry']['hasZ'], True)

        esri_spec = Geometry(geometry=multilinestring, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'],
            2056)
        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertEqual(
            esri_spec_copy['geometry']['spatialReference']['wkid'],
            2056)
        self.assertToShape(multilinestring, esri_spec, esri_spec_copy)

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

        polygon = geometry.Polygon(
            [(0, 0, 5), (1, 1, 5), (2, 1, 5), (0, 0, 5)])
        esri_spec = Geometry(geometry=polygon)
        self.assertEqual(esri_spec['geometry']['rings'][0][0][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][0][1][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][0][2][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][0][3][2], 5)
        self.assertEqual(esri_spec['geometry']['hasZ'], True)

        esri_spec = Geometry(geometry=polygon, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'], 2056)
        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertEqual(
            esri_spec_copy['geometry']['spatialReference']['wkid'], 2056)
        self.assertToShape(polygon, esri_spec, esri_spec_copy)

    def test_multipolygon(self):
        polygons = [geometry.Polygon([(0, 0), (1, 1), (2, 1), (0, 0)]),
                    geometry.Polygon([(3, 3), (4, 4), (5, 3), (3, 3)])]
        multipolygon = geometry.MultiPolygon(polygons)
        esri_spec = Geometry(geometry=multipolygon)
        self.assertEqual(len(esri_spec['geometry']['rings']), 2)
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
        self.assertEqual(esri_spec['geometry']['rings'][1][0][0], 3)
        self.assertEqual(esri_spec['geometry']['rings'][1][0][1], 3)
        self.assertEqual(esri_spec['geometry']['rings'][1][1][0], 4)
        self.assertEqual(esri_spec['geometry']['rings'][1][1][1], 4)
        self.assertEqual(esri_spec['geometry']['rings'][1][2][0], 5)
        self.assertEqual(esri_spec['geometry']['rings'][1][2][1], 3)
        self.assertEqual(esri_spec['geometry']['rings'][1][3][0], 3)
        self.assertEqual(esri_spec['geometry']['rings'][1][3][1], 3)
        self.assertNotIn('spatialReference', esri_spec['geometry'])

        polygons = [geometry.Polygon(
                        [(0, 0, 5), (1, 1, 5), (2, 1, 5), (0, 0, 5)]),
                    geometry.Polygon(
                        [(3, 3, 5), (4, 4, 5), (5, 3, 5), (3, 3, 5)])]
        multipolygon = geometry.MultiPolygon(polygons)
        esri_spec = Geometry(geometry=multipolygon)
        self.assertEqual(esri_spec['geometry']['rings'][0][0][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][0][1][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][0][2][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][0][3][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][1][0][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][1][1][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][1][2][2], 5)
        self.assertEqual(esri_spec['geometry']['rings'][1][3][2], 5)
        self.assertEqual(esri_spec['geometry']['hasZ'], True)

        esri_spec = Geometry(geometry=multipolygon, wkid=2056)
        self.assertEqual(
            esri_spec['geometry']['spatialReference']['wkid'], 2056)
        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertEqual(
            esri_spec_copy['geometry']['spatialReference']['wkid'], 2056)
        self.assertToShape(multipolygon, esri_spec, esri_spec_copy)
