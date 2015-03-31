import sys
import csv
import json


def convert_to_json():
    with open(sys.argv[1], 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        return [row for row in reader]


print json.dumps(convert_to_json(), indent=2)
