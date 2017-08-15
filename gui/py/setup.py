import os.path
import sys

from cx_Freeze import Executable, setup


def include_files():
    include_files = []
    for root_dir_path in ('src',):
        for dir_path, subdir_names, file_names in os.walk(root_dir_path):
            for file_name in file_names:
                if not file_name.endswith('.py'):
                    continue
                include_files.append(os.path.join(dir_path, file_name))
    return include_files


setup(name="PastPy",
      version='1.0.1',
      description="PastPy GUI",
      options={
          'build_exe': {
              'packages': ['os', 'wx'],
              'include_files': include_files(),
              'include_msvcr': True
          }
      },
      # , icon="static/example.ico")])
      executables=[Executable(
          base='Win32GUI' if sys.platform == 'win32' else None,
          script="src/pastpy_gui/app.py",
          targetName='pastpy.exe'
        )]
      )
