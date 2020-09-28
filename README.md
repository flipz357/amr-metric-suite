# amr-metric-suite 
This project collects a state-of-the-art tracker table for AMR parsers and AMR graph matching metrics. 
It accompanies the *[TACL paper "AMR similarity metrics from principles](https://transacl.org/index.php/tacl/article/view/2205/545)*.

## Content of this repo

1. Scripts for calculating Smatch and S2match (Soft Semantic match, speak [estuːmætʃ]).
And scripts for calculating the structure error of two AMR graph banks. 

2. Current state-of-the-art performacne of AMR parsers wrt to these metrics and some additional information.


## run Smatch or S2match with python2 and python3 

### Preparations

for S2match, word vectors (e.g. Glove) need to be downloaded and stored in the vectors/ directory:

e.g.:

```
./download_glove.sh
```

and we need to install python packages *scipy* and *numpy* (for similarity calculation) and *networkx* and *penman* to calculate graph structure error.

### Quickstart, extensive AMR evaluation

Using python 2.7:

```
./easy_eval_py2.sh <file1> <file2>
```

Using python 3.x:

```
./easy_eval_py3.sh <file1> <file2>
```

*filex* is a file in standard AMR format, i.e., AMRs separated by empty line. See examples/ for examples.

### More details (e.g. run only s2match with different vectors)

see *py2-Smatch-and-S2match* or *py3-Smatch-and-S2match*


## AMR state-of-the-art

### System IDs and short description

STOG: Graph prediction, MST-decoding (see below for reference)
GPLA: Graph prediction with latent alignment (see below for reference)
TOP-DOWN: Incremental root-to-leaf build up (see below for reference)


#### Evaluation Results on AMR 2.0 test (higher=better)

| System       | Smatch  | S2match   | Year     | Code available |
| ---          | ---     | ---       | ---      | ---            | 
| GSII         | 80.1    | 81.5      | 2020     | [yes](https://github.com/jcyk/AMR-gs)          |
| GSII-noRecat | 78.6    | 79.9      | 2020     | [yes](https://github.com/jcyk/AMR-gs)          |
| STOG-BERT    | 76.3,   | 77.9      | 2019     | [yes](https://github.com/sheng-z/stog)            |
| STOG         | 74.6,   | ?         | 2019     | [yes](https://github.com/sheng-z/stog)            |
| GPLA         | 74.5,   | 76.2      | 2018     | [yes](https://github.com/ChunchuanLv/AMR_AS_GRAPH_PREDICTION)            |      
| TOP-DOWN     | 73.2,   | 75.0      | 2019     | [yes](https://github.com/jcyk/AMR-parser)             |       


#### Structure error evaluation on AMR 2.0 test (lower=better)

| System       | Degree  | Density   |  size(V)     | size(E)    |
| ---          | ---     | ---       | ---          | ---        | 
| GSII         | 0.071   | 0.0070    | 1.87         | 2.59       |
| GPLA         | 0.083   | 0.0068    | 1.99         | 2.90       |      
| GSII-noRecat | 0.102   | 0.0073    | 2.14         | 2.75       |
| STOG-BERT    | 0.082   | 0.0069    | 2.42         | 3.19       |
| STOG         | ?       | ?         | ?            |  ?         |
| TOP-DOWN     | 0.110   | 0.0078    | 2.37         | 3.32       |       


#### System dependencies


| System        | word-embedding type | copying (src)      | copying (tgt)      | attention (src)      | attention (tgt)      | PrePro                         | recategorize | anon | notes                |
| ---           | ---                 | ---                | ---                | ---                  | ---                  | ---                            | ---          | ---  | ---                  |
| GSII          | BERT                | yes                | no                 | yes                  | yes                  | CoreNLP, lemma/pos/ner         | yes          | yes  | same pre/post proc as STOG | 
| GSII-noRecat  | BERT                | yes                | no                 | yes                  | yes                  | CoreNLP, lemma/pos/ner         | no           | no   |                      |
| STOG-BERT     | BERT                | yes                | yes                | yes                  | yes                  | CoreNLP, lemma/pos/ner         | yes          | yes  |                      |
| STOG          | GloVe 300d          | yes                | yes                | yes                  | yes                  | CoreNLP, lemma/pos/ner         | yes          | yes  |                      |
| GPLA          | Glove 300d          | yes                | no                 | no                   | no                   | CoreNLP, lemma/pos/ner         | yes          | no   |                      |
| TOP-DOWN      | Glove 300d          | yes                | no                 | yes                  | no                   | CoreNLP, lemma/pos/ner         | no           | no   |                      |


## References

GSII: Deng Cai and Wai Lam. "AMR Parsing via Graph-Sequence Iterative Inference". arXiv preprint arXiv:2004.05572 (2020). [github](https://github.com/jcyk/AMR-gs)

GPLA: Chunchuan Lyu and Ivan Titov. "Amr parsing as graph prediction with latent alignment." arXiv preprint arXiv:1805.05286 (2018). [github](https://github.com/ChunchuanLv/AMR_AS_GRAPH_PREDICTION)

STOG: Sheng Zhang et al. "AMR Parsing as Sequence-to-Graph Transduction." arXiv preprint arXiv:1905.08704 (2019). [github](https://github.com/sheng-z/stog)

TOP-DOWN: Deng Cai and Wai Lam. "Core Semantic First: A Top-down Approach for AMR Parsing." arXiv preprint arXiv:1909.04303 (2019). [github](https://github.com/jcyk/AMR-parser)

Smatch: Shu Cai and Kevin Knight. "Smatch: an evaluation metric for semantic feature structures." Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). 2013.

S2match: Juri Opitz et al. "AMR Similarity Metrics from Principles" arXiv preprint arXiv:2001.10929 (2020).


## Citation 

If you like the idea please consider citing

```
article{TACL2205,
	author = {Juri Opitz and Anette Frank and Letitia Parcalabescu},
	title = {AMR Similarity Metrics from Principles},
	journal = {Transactions of the Association for Computational Linguistics},
	volume = {8},
	number = {0},
	year = {2020},
	keywords = {},
	abstract = {Different metrics have been proposed to compare Abstract Meaning Representation (AMR) graphs. The canonical SMATCH metric (Cai and Knight, 2013) aligns the variables of two graphs and assesses triple matches. The recent SEMBLEU metric (Song and Gildea, 2019) is based on the machine-translation metric BLEU (Papineni et al., 2002) and increases computational efficiency by ablating the variable-alignment.In this paper, i) we establish criteria that enable researchers to perform a principled assessment of metrics comparing meaning representations like AMR; ii) we undertake a thorough analysis of SMATCH and SEMBLEU where we show that the latter exhibits some undesirable properties.  For example, it does not conform to the identity of indiscernibles rule and introduces biases that are hard to control; iii) we propose a novel metric S2MATCH that is more benevolent to only very slight meaning deviations and targets the fulfilment of all established criteria. We assess its suitability and show its advantages over SMATCH and SEMBLEU. },
	issn = {2307-387X},	pages = {522--538},	url = {https://transacl.org/index.php/tacl/article/view/2205}
}
``` 

## Changelog

Basis: extended Smatch metrics cloned from [Lyu's extended Smatch metric repository](https://github.com/ChunchuanLv/amr-evaluation-tool-enhanced) 
that again had been adapted from [Marco Damonte's extended metrics](https://github.com/mdtux89/amr-evaluation).

### Major consecutive changes

1. added s2match
2. added script to calculate graph structure deviation (see *graph-strucutre-error*)
3. adapted for calculating extended metrics with s2match alignment (see *scores-enhanced-s2align.py*)
4. Improved extended metrics for single-graph comparison. Previously: if A (e.g, predicted graph) 
and B (e.g., gold graph) both have a feature absent (e.g., they do not contain a polarity edge) 
---> default score for polarity 0.0. Now: this default score is changed to 1.0, 
since both A and B agree in the absence of polarity. *This is highly unlikely to have an effect on corpus-level evaluation.*
5. copied all python2 scripts and made them python3 compatible

 
