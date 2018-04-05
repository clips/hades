"""A featurizer for dictionaries."""
from __future__ import division
from __future__ import print_function

import re

from codecs import open
from collections import Counter


class DictFeaturizer(object):
    """
    Featurize text by looking up words in dictionary categories.

    Usually, the dictionary categories are built in such a way that
    semantically or functionally similar words are grouped together.

    A good example of an application of such a Featurizer is the counting of
    swear words in a text for the detection of toxic behavior on social media.
    When naively counting these words, without grouping them beforehand, a
    machine learner might not discover that swear words are similar to each
    other.

    Parameters
    ----------
    dictionary : dict
        The dictionary to use. Each dictionary should have a string as key,
        and a list of words as value. These lists of words may contain
        wilcards in the form of '*' and '+'. These conform to their meanings in
        regular expressions, i.e., '*' implies that the wildcard may occur,
        while the '+' implies that it should occur.
    relative : bool
        Whether to return absolute or relative frequencies.

    Attributes
    ----------
    dict : dict
        A dictionary of tuples, the first item of each tuple contains a list
        of normal words, while the second item of each tuple is a list of words
        with wildcards.

    """

    def __init__(self, dictionary, relative=True):
        """Initialize the DictFeaturizer."""
        self.dict = {}
        self.rel = relative
        matcher = re.compile(r'([\*\+])')

        for key, words in dictionary.items():

            normal = {x for x in words if not matcher.findall(x)}
            regexstring = "|".join([matcher.sub(r'\\w\1', x)
                                    for x in words if x not in normal])

            if regexstring:
                wildcards = re.compile(regexstring)
            else:
                wildcards = None

            self.dict[key] = (normal, wildcards)

    def transform(self, tokens):
        """Featurize a list of tokens."""
        # Make frequency dictionary of the text to diminish number
        # of runs in further for loop
        freq_dict = Counter(tokens)
        features = dict()

        for key, wordlists in self.dict.items():

            normal, wildcards = wordlists

            keys = set(freq_dict.keys())

            features[key] = sum([freq_dict[k] for k in normal & keys])
            if wildcards:
                features[key] += sum([freq_dict[k] for k in keys - normal
                                      if wildcards.match(k)])

        if self.rel:
            return {k: v / len(tokens) for k, v in features.items()}
        else:
            return features

    @staticmethod
    def load(path, relative=True):
        """
        Load a dictionary from a .csv.

        The first word of each line is the category name, the other words are
        items for that category.

        Parameters
        ----------
        path : str
            The path to the .csv
        relative : bool
            Whether to return relative or absolute frequencies.

        Returns
        -------
        d : DictFeaturizer
            An initialized dictfeaturizer

        """
        d = {}
        with open(path, "r", encoding='utf-8') as f:
            for line in f:
                line = line.lower().strip().split(",")
                key, words = line[0], set(line[1:])
                d[key] = words

        return DictFeaturizer(d, relative=relative)
