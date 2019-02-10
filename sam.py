# - *- coding: utf- 8 - *-
import io
import json
import re
import sys
import os


def main():

    LENGTH = 4
    FILEPATH = 'slowa.txt'

    if not os.path.isfile(FILEPATH):
        print("File path {} does not exist. Exiting...".format(FILEPATH))
        sys.exit()

    cores = {}

    letters = re.compile(r"[bcćdfghjklłmnńprstwxzźż]{" + str(LENGTH) + ",}", re.UNICODE)
    doubles = re.compile(r"rz|cz|sz|dz|dź|dż|ch", re.UNICODE)

    with io.open(FILEPATH, mode="r", encoding="utf-8") as fp:
        cnt = 0
        for line in fp:
            for frag in letters.findall(line):
                if len(frag) - len(doubles.findall(frag)) >= LENGTH:
                    cores.setdefault(frag.upper(), []).append(line.strip())
                    cnt += 1

    save(cores)

    print("Number of unique words: {}".format(cnt))


def save(items):
    for key in items.keys():
        items[key] = list(sorted(items[key]))
    file = io.open('out.txt', mode="w", encoding="utf-8")
    file.write(json.dumps(dict(sorted(items.items())), ensure_ascii=False))
    file.close()


if __name__ == '__main__':
    main()


