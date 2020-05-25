# amr-metric-suite 
This project collects a state-of-the-art tracker table for AMR parsers and AMR graph matching metrics. 
It accompanies the *TACL paper "AMR similarity metrics from principles (2020, to appear)"*.

## Content of this repo

Scripts for calculating Smatch and S2match.
And scripts for calculating the structure error of two AMR graph banks. 

Current state-of-the-art performacne of AMR parsers wrt to these metrics and some additional information.


## AMR state-of-the-art

### System IDs and short description

STOG: Graph prediction, MST-decoding (see below for reference)
GPLA: Graph prediction with latent alignment (see below for reference)
TOP-DOWN: Incremental root-to-leaf build up (see below for reference)


#### Evaluation Results on AMR 2.0 test (higher=better)

| System     | Smatch  | S2match   | Year     | Code available |
| ---        | ---     | ---       | ---      | ---            | 
| STOG-BERT  | 76.3,   | 77.7      | 2019     | yes            |
| STOG       | 74.6,   | ?         | 2019     | yes            |
| GPLA       | 74.5,   | 76.1      | 2018     | yes            |      
| TOP-DOWN   | 73.2,   | 74.9      | 2019     | no             |       

Remarks:

1. S2match (Soft Semantic match, speak [estuːmætʃ]) is parametrized with GloVe 100d


#### Structure error evaluation on AMR 2.0 test (lower=better)

| System     | Degree  | Density   |  size(V)     | size(E)    |
| ---        | ---     | ---       | ---          | ---        | 
| GPLA       | 0.083,  | 0.0068    | 1.99         | 2.90       |      
| STOG-BERT  | 0.082,  | 0.0069    | 2.42         | 3.19       |
| STOG       | ?       | ?         | ?            |  ?         |
| TOP-DOWN   | 0.110   | 0.0078    | 2.37         | 3.32       |       


#### System dependencies


| System  | word-embedding type | copying (src)      | copying (tgt)      | attention (src)      | attention (tgt)      | PrePro                         | recategorize | anon |
| ---     | ---                 | ---                | ---                | ---                  | ---                  | ---                            | ---          | ---  |
| STOG-BERT  | BERT             | yes                | yes                | yes                  | yes                  | CoreNLP, lemma/pos/ner         | yes          | yes  |
| STOG       | GloVe 300d       | yes                | yes                | yes                  | yes                  | CoreNLP, lemma/pos/ner         | yes          | yes  |
| GPLA       | Glove 300d       | yes                | no                 | no                   | no                   | CoreNLP, lemma/pos/ner         | yes          | no   |
| TOP-DOWN   | random           | yes                | no                 | yes                  | no                   | CoreNLP, lemma/pos/ner         | no           | no   |



## run Smatch or S2match with python2 and python3 

### Preparations

for S2match, word vectors (e.g. Glove) need to be downloaded and stored in the vectors/ directory:

e.g.:

```
download_glove.sh
```

and we need to install python packages *scipy* and *numpy* (for similarity calculation) and *networkx* and *penman* to calculate graph structure error.

### Quickstart, extensive AMR evaluation

Using python 2.7:

```
./easy_eval_py2.sh
```

Using python 3.x:

```
./easy_eval_py3.sh
```

### More details (e.g. run only s2match with different vectors)

see *py2-Smatch-and-S2match* or *py3-Smatch-and-S2match*

## run structure error with python2 and python3 

see *graph-structure-error*

## References


GPLA: Lyu, Chunchuan, and Ivan Titov. "Amr parsing as graph prediction with latent alignment." arXiv preprint arXiv:1805.05286 (2018). [github](https://github.com/ChunchuanLv/AMR_AS_GRAPH_PREDICTION)

STOG: Zhang, Sheng, et al. "AMR Parsing as Sequence-to-Graph Transduction." arXiv preprint arXiv:1905.08704 (2019). [github](https://github.com/sheng-z/stog)

TOP-DOWN: Cai, Deng, and Wai Lam. "Core Semantic First: A Top-down Approach for AMR Parsing." arXiv preprint arXiv:1909.04303 (2019). [github](https://github.com/sheng-z/stog)(https://github.com/jcyk/AMR-parser)

Smatch: Cai, Shu, and Kevin Knight. "Smatch: an evaluation metric for semantic feature structures." Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers). 2013.

S2match: Opitz, Juri et al. "AMR Similarity Metrics from Principles" arXiv preprint arXiv:2001.10929 (2020).


## Citation of this work


```
@misc{opitz2020amr,
    title={AMR Similarity Metrics from Principles},
    author={Juri Opitz and Letitia Parcalabescu and Anette Frank},
    year={2020},
    eprint={2001.10929},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
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

 
