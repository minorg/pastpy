from site_generator import SiteGenerator
import tempfile
import unittest


class SiteGeneratorTest(unittest.TestCase):
    def testGenerate(self):
        with tempfile.TemporaryDirectory() as tempdir:
            SiteGenerator(
                output_dir_path=tempdir,
                pp_install_dir_path='c:\\pp5eval'
            ).generate()


if __name__ == '__main__':
    unittest.main()