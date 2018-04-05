# HADES

This is a work-in-progress repository for the CLiPS HAte speech DEtection System (HADES).

Currently, the repository contains the supplementary materials from the paper: "A Dictionary-based Approach to Racism Detection in Dutch Social Media", presented at the [TA-COS](http://www.ta-cos.org) workshop at LREC 2016.

## license

The dictionaries in this repository are available under a [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) License.
If you use the dictionaries in your work, please cite:

```
@inproceedings{tulkens2016a,
  title={A Dictionary-based Approach to Racism Detection in {Dutch} Social Media},
  author={Tulkens, St\'{e}phan and Hilte, Lisa and Lodewyckx, Elise and Verhoeven, Ben and Daelemans, Walter},
  booktitle={Proceedings of the LREC 2016 Workshop on Text Analytics for Cybersecurity and Online Safety (TA-COS)},
  year={2016},
  organization={European Language Resources Association (ELRA)}
}
```

Note that we expanded the TA-COS submission into a journal paper, which was published in the [CLIN Journal](http://www.clinjournal.org/sites/clinjournal.org/files/Tulkens2016.pdf).

If you use the dictionary expansion techniques from this paper, please also consider citing it:

```
@article{tulkens2016automated,
  title={The automated detection of racist discourse in dutch social media},
  author={Tulkens, St{\'e}phan and Hilte, Lisa and Lodewyckx, Elise and Verhoeven, Ben and Daelemans, Walter},
  journal={Computational Linguistics in the Netherlands Journal},
  volume={6},
  number={1},
  pages={3--20},
  year={2016}
}
```

## usage

The dictionaries are in .csv format.
The first word of each line is the category name, while the other words are the words in that category.
Included is a python (2.7 & 3.x) script which reads in the dictionaries and outputs relative frequencies.
It can be used for similar dictionaries, such as the LIWC dictionaries.

## example

```python
from dictfeaturizer import DictFeaturizer

# Load from csv
d = DictFeaturizer.load("expanded.csv")
text = "this is an example text".split()
score = d.transform(text)

# Direct initialization
direct = {"good": ["good", "splendid"], "bad": ["bad", "useless"]}
d = DictFeaturizer(direct, relative=False)
text = "This stuff is splendid".split()
score_2 = d.transform(text)
```
