from argparse import ArgumentParser
import logging

try:
    __import__("pastpy")
except ImportError:
    import os.path
    import sys
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from pastpy.past_perfect_database import PastPerfectDatabase


def parse_args():
    argument_parser = ArgumentParser()
    argument_parser.add_argument("--dir-path", help="path for data files")

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

    download_subparser = subparsers.add_parser("download")
    download_subparser.add_argument("collection_name", help="collection name of PastPerfect Online site e.g., yourcollection in http://yourcollection.pastperfectonline.com")
    download_subparser.set_defaults(command="download")

    download_subparser = subparsers.add_parser("parse-html")
    download_subparser.add_argument("collection_name", help="collection name of PastPerfect Online site e.g., yourcollection in http://yourcollection.pastperfectonline.com")
    download_subparser.set_defaults(command="parse-html")

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


if args.command == "download":
    PastPerfectDatabase.create_from_online(collection_name=args.collection_name, download_dir_path=args.dir_path).download()
elif args.command == "parse-html":
    for object_detail in PastPerfectDatabase.create_from_online(collection_name=args.collection_name, download_dir_path=args.dir_path).parse_object_details():
        print(object_detail.id)
