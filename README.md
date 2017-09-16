# AnatEM Tools

This repository regroups some resources for [AnatEM](http://nactem.ac.uk/anatomytagger/) corpus processing.

## Regroup files

Regroup each corpus part (*train*, *dev*, *test*) into one file.

```bash
python main.py REGROUP \
    --input_path /path/to/original-data/AnatEM-1.0.2/conll/train \
    --output_file /path/to/output/train.conll
    
python main.py REGROUP \
    --input_path /path/to/original-data/AnatEM-1.0.2/conll/dev \
    --output_file /path/to/output/dev.conll
    
python main.py REGROUP \
    --input_path /path/to/original-data/AnatEM-1.0.2/conll/test \
    --output_file /path/to/output/test.conll
```

## Lowercase and replace digits

Lowercase and replace digits in each corpus part file.

```bash
python main.py PREPROC \
    --input_file /path/to/data/train.conll \
    --output_file /path/to/output/train-lc-dr.conll
    
python main.py PREPOC \
    --input_file /path/to/data/dev.conll \
    --output_file /path/to/output/dev-lc-dr.conll
    
python main.py PREPROC \
    --input_file /path/to/data/test.conll \
    --output_file /path/to/output/test-lc-dr.conll
```

## Transform multi-class IOB scheme into one-class IOB scheme

```bash
python main.py CONVERT \
    --input_file /path/to/data/train-lc-dr.conll \
    --output_file /path/to/output/train-lc-dr-mono.conll
    
python main.py CONVERT \
    --input_file /path/to/data/dev-lc-dr.conll \
    --output_file /path/to/output/dev-lc-dr-mono.conll
    
python main.py CONVERT \
    --input_file /path/to/data/test-lc-dr.conll \
    --output_file /path/to/output/test-lc-dr-mono.conll
```

## Add CoreNLP features

Adding several CoreNLP features to the files:
* Lemma
* Named Entity Recognition
* Part-of-Speech tags

```bash
python main.py CORENLP \
    --input_file /path/to/data/train.conll \
    --output_file /path/to/output/train-corenlp.conll
    --corenlp_url http://localhost:9000
    
python main.py CORENLP \
    --input_file /path/to/data/dev.conll \
    --output_file /path/to/output/dev-corenlp.conll
    --corenlp_url http://localhost:9000
    
python main.py CORENLP \
    --input_file /path/to/data/test.conll \
    --output_file /path/to/output/test-corenlp.conll
    --corenlp_url http://localhost:9000
```