import unittest


class _DatabaseTest(unittest.TestCase):
    def __init__(self, *args, **kwds):
        unittest.TestCase.__init__(self, *args, **kwds)
        self._database = None

    def test_objects(self):
        if self._database is None:
            return

        for object_ in self._database.objects():
            return
        self.fail()
