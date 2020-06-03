# - *- coding: utf- 8 - *-
import io
import json
import re


class Parole:
    def __init__(self, length):
        self.length = length
        self.consonants = re.compile(r"[bcćdfghjklłmnńprstwxzźż]{" + str(length) + ",}", re.UNICODE)
        self.doubles = re.compile(r"rz|cz|sz|dz|dź|dż|ch", re.UNICODE)
        self.filepath = 'slowa.txt'

    def get(self):
        cores = {}
        with io.open(self.filepath, mode="r", encoding="utf-8") as fp:
            for line in fp:
                for frag in self.consonants.findall(line):
                    if len(frag) - len(self.doubles.findall(frag)) >= self.length:
                        cores.setdefault(frag.upper(), []).append(line.strip())
        return cores

    def show(self, items):
        print(self.json(items))

    def save(self, items):
        with io.open('parole_{}_consonants.txt'.format(self.length), mode="w", encoding="utf-8") as fp:
            fp.write(self.json(items))

    @staticmethod
    def json(items):
        return json.dumps(items, indent=2, ensure_ascii=False, sort_keys=True)
