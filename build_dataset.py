import pandas as pd
from features import extract_features

df = pd.read_csv("data/malicious_phish.csv")
df = df.drop_duplicates(subset="url").reset_index(drop=True)
print("After dedup:", df.shape)

feats = pd.DataFrame([extract_features(u) for u in df["url"]])
feats["label"] = (df["type"] != "benign").astype(int)
feats["type"] = df["type"]

feats.to_csv("data/features.csv", index=False)
print(feats.shape)
print(feats["label"].value_counts())
