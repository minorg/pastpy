import os.path
import pystache
import sys

try:
    import pastpy
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'lib', 'py', 'src')))
    import pastpy


class SiteGenerator(object):
    def __init__(
        self,
        output_dir_path,
        pp_install_dir_path,
        template_dir_path=None
    ):
        self.__output_dir_path = output_dir_path
        self.__pp_install_dir_path = pp_install_dir_path
        if template_dir_path is None:
            template_dir_path = \
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'mustache'))
        self.__template_dir_path = template_dir_path

    def generate(self):
        if not os.path.isdir(self.__output_dir_path):
            os.makedirs(self.__output_dir_path)

        renderer = \
            pystache.Renderer(
                missing_tags='strict',
                search_dirs=(self.__template_dir_path,)
            )
        for file_base_name in ('index',):
            rendered = renderer.render_name(file_base_name + '.html')
            out_file_path = os.path.join(self.__output_dir_path, file_base_name + '.html')
            with open(out_file_path, 'w+') as out_file:
                out_file.write(rendered)

    @classmethod
    def main(cls):
        from argparse import ArgumentParser

        argument_parser = ArgumentParser()
        argument_parser.add_argument('-i', '--pp', dest='pp_install_dir_path', help='Path to the PastPerfect 5 installation directory e.g., C:\pp5eval')
        argument_parser.add_argument('-o', '--out', dest='output_dir_path', help="Path to the output directory")
        argument_parser.add_argument('-t', '--template', dest='template_dir_path', help="Path to the templates directory")
        args = argument_parser.parse_args()

        cls(
            output_dir_path=args.output_dir_path,
            pp_install_dir_path=args.pp_install_dir_path,
            template_dir_path=args.template_dir_path
        ).generate()


if __name__ == '__main__':
    SiteGenerator.main()
