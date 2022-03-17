import argparse
import os
import pathlib

from redactor import redactFiles


def main(args):
    print("args:", args)
    filesList = args.input
    redactObj = redactFiles()
    if args.stats:
        if not pathlib.Path(args.stats+'/stat.txt').is_file():
            try:
                os.mkdir('project1/' + args.stats)
            except OSError as dirErr:
                print("Directory already exists. So, no need to create one.")

    for fileName in filesList:
        print("file Name:", fileName)
        if fileName == "requirements.txt":
            continue
        if args.names:
            redactObj.redactNames(fileName, args.stats)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Enter type of files to be read", nargs="+", required=True)
    parser.add_argument("--names", help="if you want names to be redacted", action="store_true")
    parser.add_argument("--dates",  help="if you want dates to be redacted", action="store_true")
    parser.add_argument("--phones",  help="if you want phones to be redacted", action="store_true")
    parser.add_argument("--genders",  help="if you want genders to be redacted", action="store_true")
    parser.add_argument("--address",  help="if you want address to be redacted", action="store_true")
    parser.add_argument("--concept",  help="if you want any concept to be redacted", type=str)
    parser.add_argument("--output", help="Specify the folder name to store redacted files")
    parser.add_argument("--stats", help="Stats")
    args = parser.parse_args()
    main(args)
