import sys
import csv
with open(sys.argv[1], 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print ', '.join(row)
