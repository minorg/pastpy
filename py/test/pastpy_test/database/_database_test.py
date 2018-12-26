import unittest


class _DatabaseTest(unittest.TestCase):
    def __init__(self, *args, **kwds):
        unittest.TestCase.__init__(self, *args, **kwds)
        self._database = None

    def _test_objects(self):
        if self._database is None:
            return

        for object_ in self._database.objects():
            self.assertNotEqual(None, object_.date)
            self.assertNotEqual(None, object_.name)
            self.assertTrue(len(tuple(object_.images())))
            # self.assertTrue(object_.impl_attributes)
