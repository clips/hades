from __future__ import division
from __future__ import print_function

import re

from codecs import open
from collections import Counter


class DictFeaturizer(object):

    def __init__(self, path):

        self.dict = {}
        matcher = re.compile(r'([\*\+])')

        with open(path, "r", encoding='utf-8') as f:
            for line in f:
                line = line.lower().strip().split(",")
                key, words = line[0], set(line[1:])

                normal = {x for x in words if not matcher.findall(x)}

                regexstring = "|".join([matcher.sub(r'\\w\1', x) for x in words if x not in normal])
                if regexstring:
                    regex = re.compile(regexstring)
                else:
                    regex = []

                self.dict[key] = (normal, regex)

    def featurize(self, text, rel=True):
        """
        param: text: a tokenized string representation.
        type: text: str
        return: a frequency dictionary for each category in the dictionary.
        type: return: dict
        """

        # Make frequency dictionary of the text to diminish number of runs in further for loop
        freq_dict = Counter(text.lower().split())

        features = dict()

        for key, wordlists in self.dict.items():

            normal, wildcards = wordlists
            freq = 0

            features[key] = sum([freq_dict[k] for k in normal & freq_dict.keys()]) 
            if wildcards:
                features[key] += sum([freq_dict[k] for k in freq_dict.keys() - normal if wildcards.match(k)])
            
        if rel:
            return {k: v / len(text.split()) for k, v in features.items()}
        else:
            return features