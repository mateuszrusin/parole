# - *- coding: utf- 8 - *-
import io
import json
import re
import pandas as pd


class Parole:
    def __init__(self, length, filepath='slowa.txt'):
        self.length = length
        self.consonants = re.compile(r"[bcćdfghjklłmnńprstwxzźż]", re.UNICODE)
        self.doubles = re.compile(r"rz|cz|sz|dz|dź|dż|ch", re.UNICODE)
        self.filepath = filepath

    def show(self, items):
        print(self.json(items))

    def count(self, word):
        count = i = 0
        while i < len(word):
            if self.doubles.match(word, i):
                count += 1
                i += 2
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
                if self.count(line):
                    cores.setdefault(len(line), []).append(line.strip())

        return cores

    def get_by_pandas(self):
        df = pd.read_csv(self.filepath, header=None, names=['word'], encoding='utf-8')
        df['word'] = df['word'].str.strip()

        # Filtracja słów spełniających warunki
        df['valid'] = df['word'].apply(self.count)
        valid_words = df[df['valid']]['word']

        # Grupowanie według długości słowa
        cores = valid_words.groupby(valid_words.str.len()).apply(list).to_dict()

        return cores

    @staticmethod
    def json(items):
        return json.dumps(items, indent=2, ensure_ascii=False, sort_keys=True)
