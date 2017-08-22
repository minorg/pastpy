import os.path
from site_generator import SiteGenerator
import tempfile
import unittest
import webbrowser


class SiteGeneratorTest(unittest.TestCase):
    def testGenerate(self):
        # with tempfile.TemporaryDirectory() as tempdir:
        tempdir = tempfile.mkdtemp()
        if True:
            pp_install_dir_path = 'c:\\pp5eval'
            SiteGenerator(
                output_dir_path=tempdir,
                pp_install_dir_path=pp_install_dir_path,
            ).generate()
            webbrowser.open(tempdir)
            #webbrowser.open_new(os.path.join(tempdir, 'index.html'))


if __name__ == '__main__':
    unittest.main()
