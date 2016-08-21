import argparse
import logging

from pastpy.commands.site import Site


class Main(object):
    @classmethod
    def main(cls):
        argument_parser = argparse.ArgumentParser()
        argument_parser.add_argument(
            '-d',
            '--debug',
            action='store_true',
            help='enable debug logging'
        )

        subparsers = argument_parser.add_subparsers()

        for command in (Site,):
            subparser = subparsers.add_parser(command.__name__.lower())
            command.add_arguments(subparser)
            subparser.set_defaults(command=command)

        args = argument_parser.parse_args()
        args_dict = args.__dict__

        logging_kwds = {
            'format': '%(asctime)s:%(module)s:%(lineno)s:%(name)s:%(levelname)s: %(message)s',
            'level': logging.WARN
        }  # @IgnorePep8
        if args_dict.pop('debug', None):
            logging_kwds['level'] = logging.DEBUG
        logging.basicConfig(**logging_kwds)

        command = args_dict.pop('command')
        command(**args_dict)()

def main():
    Main.main()

if __name__ == '__main__':
    Main.main()