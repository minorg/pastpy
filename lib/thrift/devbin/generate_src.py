import os.path
import shutil
import sys

try:
    __import__('thryft')
    raise RuntimeError('thryft should not be on the PYTHONPATH already')
except ImportError:
    pass

MY_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR_PATH = os.path.abspath(os.path.join(MY_DIR_PATH, '..', '..'))
THRYFT_ROOT_DIR_PATH = os.path.abspath(os.path.join(ROOT_DIR_PATH, '..', '..', 'thryft'))
assert os.path.isdir(THRYFT_ROOT_DIR_PATH), THRYFT_ROOT_DIR_PATH
sys.path.insert(0, os.path.join(THRYFT_ROOT_DIR_PATH, 'compiler', 'src'))

import thryft.main
from thryft.generators.lint.lint_generator import LintGenerator
from thryft.generators.py.py_generator import PyGenerator


class Main(thryft.main.Main):
    def __init__(self, **kwds):
        thryft.main.Main.__init__(
            self,
            document_root_dir_path=os.path.join(ROOT_DIR_PATH, 'thrift', 'src'),
            include_dir_paths=(
                os.path.join(ROOT_DIR_PATH, 'thrift', 'src'),
            ),
            **kwds
        )

    def _clean(self):
        for dir_path in (
             os.path.join(ROOT_DIR_PATH, 'py', 'src', 'pastpy', 'models'),
        ):
            if os.path.isdir(dir_path):
                shutil.rmtree(dir_path)

    def _compile(self):
        for thrift_file_path in self._get_thrift_file_paths(self.document_root_dir_path):
            compile_kwds = {
                'thrift_file_path': thrift_file_path
            }

            self._compile_thrift_file(
                generator=LintGenerator(),
                **compile_kwds
            )

            self._compile_thrift_file(
                generator=PyGenerator(),
                out=os.path.join(ROOT_DIR_PATH, 'py', 'src'),
                **compile_kwds
            )

assert __name__ == '__main__'
Main.main()
