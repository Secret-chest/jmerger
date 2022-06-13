#!/usr/bin/python3
"""
Example usage:
./jmerger.py sampleJSON/1.json sampleJSON/2.json sampleJSON/3.json -f output.json
"""

import sys
import argparse
import json

parser = argparse.ArgumentParser(description="Merge JSON files.")


parser.add_argument("-f", "--file", dest="outputFile", default="stdout",
                    help="write output to FILE instead of stdout")
parser.add_argument("-i", "--indentation", dest="indent", default=4,
                    help="set custom indentation for output, default 4")
parser.add_argument("-q", "--quiet",
                    action="store_true", dest="quiet", default=False,
                    help="only print the JSON output (if applicable) to stdout, otherwise print nothing")
parser.add_argument("files", nargs="*")

args = parser.parse_args()

files = args.files
if len(files) < 2:
    print("need at least 2 files", file=sys.stderr)
    exit(1)
if not args.quiet:
    print(f"merging { len(files) } files { files } into { args.outputFile }")
outputFile = open(str(args.outputFile if args.outputFile != "stdout" else sys.stdout), "w")

newJSONData = {}
for file in files:
    data = json.load(open(file))
    for k in data.keys():
        newJSONData[k] = data[k]
if args.outputFile == "stdout":
    print(json.dumps(newJSONData, indent=args.indent), file=sys.stdout)
else:
    print(json.dumps(newJSONData, indent=args.indent), file=outputFile)

outputFile.close()
