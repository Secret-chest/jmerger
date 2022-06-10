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
parser.add_argument("-q", "--quiet",
                    action="store_true", dest="quiet", default=False,
                    help="only print the JSON output (if applicable) to stdout, otherwise print nothing")
parser.add_argument("files", nargs="*")

args = parser.parse_args()

files = args.files
if len(files) < 2:
    print("need at least 2 files", file=sys.stderr)
    exit(1)
print(f"merging { len(files) } files { files } into { args.outputFile }")
outputFile = open(str(args.outputFile if args.outputFile != "stdout" else sys.stdout), "w")

newJSONData = {}
for file in files:
    data = json.load(open(file))
    for k in data.keys():
        newJSONData[k] = data[k]
json.dump(newJSONData, outputFile)
outputFile.close()
