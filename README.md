# anatem-tools

## Regroup files

Regroup each corpus part (*train*, *dev*, *test*) into one file.

```bash
python main.py REGROUP \
    --input_path /path/to/original-data/AnatEM-1.0.2/conll/train \
    --output_path /path/to/output/train.conll
    
python main.py REGROUP \
    --input_path /path/to/original-data/AnatEM-1.0.2/conll/dev \
    --output_path /path/to/output/dev.conll
    
python main.py REGROUP \
    --input_path /path/to/original-data/AnatEM-1.0.2/conll/test \
    --output_path /path/to/output/test.conll
```

## Lowercase and replace digits

Lowercase and replace digits in each corpus part file.

```bash
python main.py PREPROC \
    --input_path /path/to/data/train.conll \
    --output_path /path/to/output/train-lc-dr.conll
    
python main.py PREPOC \
    --input_path /path/to/data/dev.conll \
    --output_path /path/to/output/dev-lc-dr.conll
    
python main.py PREPROC \
    --input_path /path/to/data/test.conll \
    --output_path /path/to/output/test-lc-dr.conll
```

## Transform multi-class IOB scheme into one-class IOB scheme

```bash
python main.py CONVERT \
    --input_path /path/to/data/train-lc-dr.conll \
    --output_path /path/to/output/train-lc-dr-mono.conll
    
python main.py CONVERT \
    --input_path /path/to/data/dev-lc-dr.conll \
    --output_path /path/to/output/dev-lc-dr-mono.conll
    
python main.py CONVERT \
    --input_path /path/to/data/test-lc-dr.conll \
    --output_path /path/to/output/test-lc-dr-mono.conll
```