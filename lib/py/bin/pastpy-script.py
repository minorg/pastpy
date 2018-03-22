from argparse import ArgumentParser
import json
import logging

try:
    __import__("pastpy")
except ImportError:
    import os.path
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from pastpy.database.past_perfect_database import PastPerfectDatabase


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
    subparser.add_argument("collection_name", help="collection name of PastPerfect Online site e.g., yourcollection in http://yourcollection.pastperfectonline.com")
    subparser.add_argument("--download-dir-path", help="path for downloaded files, defaults to collection name")
    subparser.set_defaults(command="download")

    subparser = subparsers.add_parser("parse-html")
    subparser.add_argument("collection_name", help="collection name of PastPerfect Online site e.g., yourcollection in http://yourcollection.pastperfectonline.com")
    subparser.add_argument("--download-dir-path", help="path for downloaded files, defaults to collection name")
    subparser.set_defaults(command="parse-html")

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


configuration = None
if os.path.isfile(args.configuration_file_path):
    with open(args.configuration_file_path, 'rb') as configuration_file:
        configuration = json.load(configuration_file)


if args.command == "download":
    PastPerfectDatabase.create_from_online(collection_name=args.collection_name, download_dir_path=args.download_dir_path).download()
elif args.command == "parse-html":
    for object_detail in PastPerfectDatabase.create_from_online(collection_name=args.collection_name, download_dir_path=args.download_dir_path).parse_object_details():
        print(object_detail.id)
elif args.command == "site":
    from pastpy.gen.site.site_configuration import SiteConfiguration
    site_configuration = SiteConfiguration.from_builtins(configuration["site"])

    from pastpy.site.site_generator import SiteGenerator
    SiteGenerator(configuration=site_configuration).generate()
