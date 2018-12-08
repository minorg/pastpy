import unittest


class _DatabaseTest(unittest.TestCase):
    def test_objects(self):
        for object_ in self._database.objects():
            return
        self.fail()
