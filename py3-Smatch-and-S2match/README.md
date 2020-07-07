# Evaluate AMR with Smatch (Semantic match) and S2match (Soft Semantic match, speak [estuːmætʃ]) for Python 2
	
## Information 

Most of this code is from https://github.com/ChunchuanLv/amr-evaluation-tool-enhanced, which is a variant of https://github.com/mdtux89/amr-evaluation.

## Usage

compute Smatch:

```
python2 smatch/smatch.py -f <prediction-file> <gold-file>
```

compute S2match with default glove 100d:

```
python2 smatch/s2match.py -f <prediction-file> <gold-file>
```

## Fine-grained metrics

Evaluation metrics to compare AMR graphs based on Smatch (http://amr.isi.edu/evaluation.html). The script computes a set of metrics between AMR graphs in addition to the traditional Smatch code:

* **Unlabeled**(differ): Smatch score computed on the predicted graphs after (canonicalizing direction and) removing all edge labels 
* No WSD. Smatch score while ignoring Propbank senses (e.g., duck-01 vs duck-02)
* Named Ent. F-score on the named entity recognition (:name roles)
* **Non_sense_frames**(new). F-score on Propbank frame identification without sense (e.g. duck-00) 
* **Frames**(new). F-score on Propbank frame identification without sense (e.g. duck-01)
* Wikification. F-score on the wikification (:wiki roles)
* Negations. F-score on the negation detection (:polarity roles)
* Concepts. F-score on the concept identification task
* Reentrancy. Smatch computed on reentrant edges only
* SRL. Smatch computed on :ARG-i roles only

The different metrics were introduced in the paper below, which also uses them to evaluate several AMR parsers:

"An Incremental Parser for Abstract Meaning Representation", Marco Damonte, Shay B. Cohen and Giorgio Satta. Proceedings of EACL (2017). URL: https://arxiv.org/abs/1608.06111

**(Some of the metrics were recently fixed and updated)**

**Smatch fine-grained Usage with fix** ```./evaluation-fixed-smatch.sh <parsed data> <gold data>```

**S2match fine-grained Usage with fix** ```./evaluation-fixed-s2match.sh <parsed data> <gold data>```


## Fixes

**Fix for comparing single graphs** previously, if e.g., gold graph has no negation and atuomatic graph has no negation, then Smatch was set to 0. With the fix, Smatch is set to 1, in those scenarios. This should not have any effects on corpus level evaluation.


