from tests import BaseTestClass
from esrijson import Feature


class TestFeature(BaseTestClass):

    def test_feature(self):
        point = self.getPoint()
        attributes = {'name': 'dummy', 'population': 85}
        Feature(geometry=point, attributes=attributes)
