# -*- coding: utf-8 -*-

from tests import BaseTestClass
from esrijson import Geometry, Feature, dumps, loads


class TestFeature(BaseTestClass):

    def test_codecs(self):
        geom = self.getPoint()
        geom_json = dumps(geom)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"y": 1.0, "x": 0.0}')
        self.assertPoint(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getPoint(hasZ=True)
        geom_json = dumps(geom)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"y": 1.0, "x": 0.0, "z": 5.0}')
        self.assertPoint(geom_esri, hasZ=True)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getMultiPoint()
        geom_json = dumps(geom)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"points": [[0.0, 1.0], [1.0, 2.0]]}')
        self.assertMultiPoint(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getLineString()
        geom_json = dumps(geom)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"paths": [[[0.0, 0.0], [1.0, 1.0]]]}')
        self.assertLineString(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getMultiLineString()
        geom_json = dumps(geom)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"paths": ' +
                                    '[[[0.0, 0.0], [1.0, 1.0]], ' +
                                    '[[-1.0, 0.0], [1.0, 0.0]]]}')
        self.assertMultiLineString(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getPolygon()
        geom_json = dumps(geom)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"rings": [[[0.0, 0.0], [1.0, 1.0], ' +
                                    '[2.0, 1.0], [0.0, 0.0]]]}')
        self.assertPolygon(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        geom = self.getMultiPolygon()
        geom_json = dumps(geom)
        geom_esri = loads(geom_json)
        self.assertEqual(geom_json, '{"rings": [[[0.0, 0.0], [1.0, 1.0], ' +
                                    '[2.0, 1.0], [0.0, 0.0]], ' +
                                    '[[3.0, 3.0], [4.0, 4.0], ' +
                                    '[5.0, 3.0], [3.0, 3.0]]]}')
        self.assertMultiPolygon(geom_esri)
        self.assertIsInstance(geom_esri, Geometry)

        feat = Feature(attributes={'a': 'a'}, geometry=geom, wkid=2056)
        feat_json = dumps(feat)
        feat_esri = loads(feat_json)
        self.assertEqual(feat_json, '{"geometry": {"rings": [[[0.0, 0.0], ' +
                                    '[1.0, 1.0], [2.0, 1.0], [0.0, 0.0]], ' +
                                    '[[3.0, 3.0], [4.0, 4.0], [5.0, 3.0], ' +
                                    '[3.0, 3.0]]], ' +
                                    '"spatialReference": {"wkid": 2056}}, ' +
                                    '"attributes": {"a": "a"}}')
        self.assertMultiPolygon(feat_esri['geometry'], wkid=2056)
