import sys
import csv
import json


def all_languages_and_their_words():
    for row in csv.DictReader(open(sys.argv[1], 'r')):
        rowcopy = dict(row)
        try:
            del rowcopy['Language']
            del rowcopy['#']
            for k, v in dict(rowcopy).iteritems():
                if v == "":
                    del rowcopy[k]
        except KeyError:
            pass
        yield (row.get('Language', None), rowcopy)


def convert_to_json():
    return dict(
        (language, words)
        for (language, words) in all_languages_and_their_words()
    )


print json.dumps(convert_to_json(), indent=2)
