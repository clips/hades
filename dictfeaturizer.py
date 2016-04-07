from __future__ import division
from __future__ import print_function

import re

from codecs import open
from collections import Counter


class DictFeaturizer(object):

    def __init__(self, path, rel=True):
        """
        The dictfeaturizer featurizes a text by looking up whether specific words in the text occur in dictionaries.
        The dictionaries should be built in such a way that words that are semantically or functionally similar are
        grouped.

        :param path: The path to the dictionary file.
        :param rel: Whether the frequencies returned by the object should be relative or absolute,
        :return:
        """

        self.dict = {}
        self.rel = rel
        matcher = re.compile(r'([\*\+])')

        with open(path, "r", encoding='utf-8') as f:
            for line in f:
                line = line.lower().strip().split(",")
                key, words = line[0], set(line[1:])

                normal = {x for x in words if not matcher.findall(x)}
                regexstring = "|".join([matcher.sub(r'\\w\1', x) for x in words if x not in normal])

                if regexstring:
                    wildcards = re.compile(regexstring)
                else:
                    wildcards = None

                self.dict[key] = (normal, wildcards)

    def featurize(self, tokens):
        """
        :param: tokens: a list of tokens.
        :type: tokens: list
        :return: a frequency dictionary for each category in the dictionary.
        :type: return: dict
        """

        # Make frequency dictionary of the text to diminish number of runs in further for loop
        freq_dict = Counter(tokens)
        features = dict()

        for key, wordlists in self.dict.items():

            normal, wildcards = wordlists

            keys = set(freq_dict.keys())

            features[key] = sum([freq_dict[k] for k in normal & keys])
            if wildcards:
                features[key] += sum([freq_dict[k] for k in keys - normal if wildcards.match(k)])
            
        if self.rel:
            return {k: v / len(tokens) for k, v in features.items()}
        else:
            return features
