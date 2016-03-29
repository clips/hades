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

## usage

The dictionaries are in .csv format. The first word of each line is the category name, while the other words are words in that category. Included is a python (2.7 & 3.x) script which reads in the dictionaries and outputs relative frequencies. Can be used for similar dictionaries, such as the LIWC dictionaries.
