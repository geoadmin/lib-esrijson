from tests import BaseTestClass
from esrijson import Geometry
from shapely.geometry import box


class TestGeometry(BaseTestClass):

    def test_point(self):
        point = self.getPoint()
        esri_spec = Geometry(geometry=point)
        self.assertPoint(esri_spec['geometry'])

        point = self.getPoint(hasZ=True)
        esri_spec = Geometry(geometry=point)
        self.assertPoint(esri_spec['geometry'], hasZ=True)

        esri_spec = Geometry(geometry=point, wkid=2056)
        self.assertPoint(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertPoint(esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(point, esri_spec, esri_spec_copy)

    def test_multipoint(self):
        multipoint = self.getMultiPoint()
        esri_spec = Geometry(geometry=multipoint)
        self.assertMultiPoint(esri_spec['geometry'])

        multipoint = self.getMultiPoint(hasZ=True)
        esri_spec = Geometry(geometry=multipoint)
        self.assertMultiPoint(esri_spec['geometry'], hasZ=True)

        esri_spec = Geometry(geometry=multipoint, wkid=2056)
        self.assertMultiPoint(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertMultiPoint(esri_spec['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(multipoint, esri_spec, esri_spec_copy)

    def test_linestring(self):
        linestring = self.getLineString()
        esri_spec = Geometry(geometry=linestring)
        self.assertLineString(esri_spec['geometry'])

        linestring = self.getLineString(hasZ=True)
        esri_spec = Geometry(geometry=linestring)
        self.assertLineString(esri_spec['geometry'], hasZ=True)

        esri_spec = Geometry(geometry=linestring, wkid=2056)
        self.assertLineString(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertLineString(esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(linestring, esri_spec, esri_spec_copy)

    def test_multilinestring(self):
        multilinestring = self.getMultiLineString()
        esri_spec = Geometry(geometry=multilinestring)
        self.assertMultiLineString(esri_spec['geometry'])

        multilinestring = self.getMultiLineString(hasZ=True)
        esri_spec = Geometry(geometry=multilinestring)
        self.assertMultiLineString(esri_spec['geometry'], hasZ=True)

        esri_spec = Geometry(geometry=multilinestring, wkid=2056)
        self.assertMultiLineString(
            esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertMultiLineString(
            esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(multilinestring, esri_spec, esri_spec_copy)

    def test_polygon(self):
        # Coordinates are oriented clock-wise
        polygon = self.getPolygon()
        esri_spec = Geometry(geometry=polygon)
        self.assertPolygon(esri_spec['geometry'])

        polygon = self.getPolygon(hasZ=True)
        esri_spec = Geometry(geometry=polygon)
        self.assertPolygon(esri_spec['geometry'], hasZ=True)

        esri_spec = Geometry(geometry=polygon, wkid=2056)
        self.assertPolygon(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertPolygon(esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(polygon, esri_spec, esri_spec_copy)

    def test_multipolygon(self):
        multipolygon = self.getMultiPolygon()
        esri_spec = Geometry(geometry=multipolygon)
        self.assertMultiPolygon(esri_spec['geometry'])

        multipolygon = self.getMultiPolygon(hasZ=True)
        esri_spec = Geometry(geometry=multipolygon)
        self.assertMultiPolygon(esri_spec['geometry'], hasZ=True)

        esri_spec = Geometry(geometry=multipolygon, wkid=2056)
        self.assertMultiPolygon(esri_spec['geometry'], hasZ=True, wkid=2056)

        esri_spec_copy = Geometry(geometry=esri_spec)
        self.assertMultiPolygon(
            esri_spec_copy['geometry'], hasZ=True, wkid=2056)

        self.assertToShape(multipolygon, esri_spec, esri_spec_copy)

    def test_bbox(self):
        bbox = box(1, 1, 2, 2)
        esri_spec = {'xmin': 1, 'ymin': 1, 'xmax': 2, 'ymax': 2}
        esri_spec_alt = [1, 1, 2, 2]
        self.assertToShape(bbox, esri_spec, esri_spec_alt)
