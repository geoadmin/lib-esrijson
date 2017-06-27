from tests import BaseTestClass
from esrijson import Feature
from shapely.geometry import box, GeometryCollection


class TestFeature(BaseTestClass):

    def test_point(self):
        point = self.getPoint()
        esri_spec = Feature(geometry=point)
        self.assertPoint(esri_spec['geometry'])

        point = self.getPoint(hasZ=True)
        esri_spec = Feature(geometry=point)
        self.assertPoint(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=point, wkid=2056)
        self.assertPoint(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertPoint(esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(point, esri_spec, esri_spec_copy)

    def test_multipoint(self):
        multipoint = self.getMultiPoint()
        esri_spec = Feature(geometry=multipoint)
        self.assertMultiPoint(esri_spec['geometry'])

        multipoint = self.getMultiPoint(hasZ=True)
        esri_spec = Feature(geometry=multipoint)
        self.assertMultiPoint(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=multipoint, wkid=2056)
        self.assertMultiPoint(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertMultiPoint(esri_spec['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(multipoint, esri_spec, esri_spec_copy)

    def test_linestring(self):
        linestring = self.getLineString()
        esri_spec = Feature(geometry=linestring)
        self.assertLineString(esri_spec['geometry'])

        linestring = self.getLineString(hasZ=True)
        esri_spec = Feature(geometry=linestring)
        self.assertLineString(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=linestring, wkid=2056)
        self.assertLineString(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertLineString(esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(linestring, esri_spec, esri_spec_copy)

    def test_multilinestring(self):
        multilinestring = self.getMultiLineString()
        esri_spec = Feature(geometry=multilinestring)
        self.assertMultiLineString(esri_spec['geometry'])

        multilinestring = self.getMultiLineString(hasZ=True)
        esri_spec = Feature(geometry=multilinestring)
        self.assertMultiLineString(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=multilinestring, wkid=2056)
        self.assertMultiLineString(
            esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertMultiLineString(
            esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(multilinestring, esri_spec, esri_spec_copy)

    def test_polygon(self):
        # Coordinates are oriented clock-wise
        polygon = self.getPolygon()
        esri_spec = Feature(geometry=polygon)
        self.assertPolygon(esri_spec['geometry'])

        polygon = self.getPolygon(hasZ=True)
        esri_spec = Feature(geometry=polygon)
        self.assertPolygon(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=polygon, wkid=2056)
        self.assertPolygon(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertPolygon(esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(polygon, esri_spec, esri_spec_copy)

    def test_multipolygon(self):
        multipolygon = self.getMultiPolygon()
        esri_spec = Feature(geometry=multipolygon)
        self.assertMultiPolygon(esri_spec['geometry'])

        multipolygon = self.getMultiPolygon(hasZ=True)
        esri_spec = Feature(geometry=multipolygon)
        self.assertMultiPolygon(esri_spec['geometry'], hasZ=True)

        esri_spec = Feature(geometry=multipolygon, wkid=2056)
        self.assertMultiPolygon(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Feature(geometry=esri_spec['geometry'])
        self.assertMultiPolygon(
            esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(multipolygon, esri_spec, esri_spec_copy)

    def test_geometrycolleciton(self):
        geomcollection = GeometryCollection([self.getPoint(),
                                             self.getPolygon()])
        esri_spec = Feature(geometry=geomcollection)
        self.assertPoint(esri_spec['geometry'])

    def test_bbox(self):
        bbox = box(1, 1, 2, 2)
        esri_spec = {'xmin': 1, 'ymin': 1, 'xmax': 2, 'ymax': 2}
        esri_spec_alt = [1, 1, 2, 2]
        self.assertToShape(bbox, esri_spec, esri_spec_alt)

    def test_extra(self):
        polygon = self.getPolygon()
        esri_spec = Feature(geometry=polygon,
                            attributes={'name': 'a', 'number': 1},
                            id=2,
                            bbox=[1, 2, 4, 7])
        self.assertPolygon(esri_spec['geometry'])
        self.assertEqual(esri_spec['attributes']['name'], 'a')
        self.assertEqual(esri_spec['attributes']['number'], 1)
        self.assertEqual(esri_spec['id'], 2)
        self.assertEqual(esri_spec['bbox'][0], 1)
        self.assertEqual(esri_spec['bbox'][1], 2)
        self.assertEqual(esri_spec['bbox'][2], 4)
        self.assertEqual(esri_spec['bbox'][3], 7)
