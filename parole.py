# - *- coding: utf- 8 - *-
import io
import json
import re


class Parole:
    def __init__(self, length):
        self.length = length
        self.consonants = re.compile(r"[bcćdfghjklłmnńprstwxzźż]", re.UNICODE)
        self.doubles = re.compile(r"rz|cz|sz|dz|dź|dż|ch", re.UNICODE)
        self.filepath = 'slowa.txt'

    def show(self, items):
        print(self.json(items))

    def count_consonants(self, word):
        # Przechodzi przez słowo, zliczając spółgłoski i uwzględniając podwójne spółgłoski
        count = 0
        i = 0
        while i < len(word):
            if self.doubles.match(word, i):
                count += 1
                i += 2  # Przeskakujemy podwójną spółgłoskę
            elif self.consonants.match(word[i]):
                count += 1
                i += 1
            else:
                count = 0
                i += 1

            if count >= self.length:
                return True

        return False

    def get(self):
        cores = {}
        with io.open(self.filepath, mode="r", encoding="utf-8") as fp:
            for line in fp:
                if self.count_consonants(line):
                    cores.setdefault(len(line), []).append(line.strip())

        return cores

    @staticmethod
    def json(items):
        return json.dumps(items, indent=2, ensure_ascii=False, sort_keys=True)
