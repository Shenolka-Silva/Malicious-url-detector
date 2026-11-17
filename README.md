# AI-Powered Malicious URL Detector

A Kali Linux tool that classifies URLs as BENIGN, SUSPICIOUS, or MALICIOUS using a Random Forest model on lexical URL features, an allowlist, and the OpenPhish feed.

## Setup
    python3 -m venv venv && source venv/bin/activate
    pip install pandas numpy scikit-learn tldextract joblib flask requests kaggle six pytest
    kaggle datasets download -d sid321axn/malicious-urls-dataset -p data --unzip
    python build_dataset.py
    python train.py
    ./update_feed.sh

## Usage
    python scan.py <url> [url2 ...]
    python scan.py -f urls.txt -o results.csv
    python app.py   # web UI at http://127.0.0.1:5000

## Pipeline
1. OpenPhish feed match -> MALICIOUS
2. Trusted-domain allowlist -> BENIGN
3. Random Forest probability: below 0.35 BENIGN, 0.35 to 0.75 SUSPICIOUS, 0.75 and above MALICIOUS

## Limitations
Trained on the Kaggle Malicious URLs dataset, which has labeling biases. Use as a triage aid, not a sole security control.
