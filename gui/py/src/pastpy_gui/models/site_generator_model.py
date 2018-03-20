import os.path
from site_generator import SiteGenerator


class SiteGeneratorModel(object):
    def __init__(self):
        self.copyright_holder = SiteGenerator.COPYRIGHT_HOLDER_DEFAULT
        self.pp_install_dir_path = SiteGenerator.PP_INSTALL_DIR_PATH_EXAMPLE
        self.pp_images_dir_path = None
        self.pp_objects_dbf_file_path = None
        self.output_dir_path = os.path.join(
            os.path.expanduser("~"), "Documents", "PastPerfect site")
        self.site_name = SiteGenerator.SITE_NAME_DEFAULT
        self.templates_dir_path = SiteGenerator.TEMPLATES_DIR_PATH_DEFAULT
