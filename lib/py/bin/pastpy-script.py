assert __name__ == "__main__"
from argparse import ArgumentParser

from pastpy.impl.online.online_past_perfect_database import OnlinePastPerfectDatabase


def parse_args():
    argument_parser = ArgumentParser()
    argument_parser.add_argument("--dir-path", help="path for data files")

    subparsers = argument_parser.add_subparsers()

    online_subparser = subparsers.add_parser("download")
    online_subparser.add_argument("name", help="name of PastPerfect Online site e.g., yoursite in http://yoursite.pastperfectonline.com")
    online_subparser.set_defaults(command="download")

    return argument_parser.parse_args()


args = parse_args()


if args.command == "download":
    OnlinePastPerfectDatabase(name=args.name, dir_path=args.dir_path).download()
