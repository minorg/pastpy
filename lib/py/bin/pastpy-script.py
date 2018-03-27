from argparse import ArgumentParser
import json
import logging

try:
    __import__("pastpy")
except ImportError:
    import os.path
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from pastpy.database.database import Database
from pastpy.gen.configuration import Configuration


def parse_args():
    argument_parser = ArgumentParser()
    argument_parser.add_argument("-c", "--configuration-file-path", default=".pastpy.json")
    argument_parser.add_argument(
        '--debug',
        action='store_true',
        help='turn on debugging'
    )
    argument_parser.add_argument(
        '--logging-level',
        help='set logging-level level (see Python logging module)'
    )

    subparsers = argument_parser.add_subparsers()

    subparser = subparsers.add_parser("download")
    subparser.set_defaults(command="download")

    subparser = subparsers.add_parser("parse")
    subparser.set_defaults(command="parse")

    subparser = subparsers.add_parser("site")
    subparser.set_defaults(command="site")

    parsed_args = argument_parser.parse_args()

    if not hasattr(parsed_args, "command"):
        argument_parser.print_usage()
        raise SystemExit(0)

    if parsed_args.debug:
        logging_level = logging.DEBUG
    elif parsed_args.logging_level is not None:
        logging_level = getattr(logging, parsed_args.logging_level.upper())
    else:
        logging_level = logging.INFO
    logging.basicConfig(
        format='%(asctime)s:%(module)s:%(lineno)s:%(name)s:%(levelname)s: %(message)s',
        level=logging_level
    )

    return parsed_args


args = parse_args()


with open(args.configuration_file_path, 'rb') as configuration_file:
    configuration = Configuration.from_builtins(json.load(configuration_file))

database = Database.create(configuration=configuration.database)

if args.command == "download":
    if not hasattr(database, "download"):
        raise ValueError("configured database is not downloadable")
    database.download()
elif args.command == "parse":
    if not hasattr(database, "download"):
        raise ValueError("configured database is not parseable")
    for object_detail in database.parse_object_details():
        print(object_detail.id)
elif args.command == "site":
    if not configuration.site:
        raise ValueError("no site configured")

    from pastpy.site.site_generator import SiteGenerator
    SiteGenerator(configuration=configuration.site, database=database).generate()
