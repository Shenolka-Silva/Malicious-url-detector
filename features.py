import re
import math
from urllib.parse import urlparse
from collections import Counter
import tldextract

SUSPICIOUS_WORDS = ["login", "verify", "secure", "account", "update", "bank",
                    "paypal", "signin", "confirm", "password", "free", "bonus"]

def entropy(s):
    if not s:
        return 0.0
    counts = Counter(s)
    return -sum((c / len(s)) * math.log2(c / len(s)) for c in counts.values())

def extract_features(url):
    url = str(url).strip()
    try:
        parsed = urlparse(url if "://" in url else "http://" + url)
        parsed.port
    except ValueError:
        parsed = urlparse("http://invalid.invalid")
    ext = tldextract.extract(url)
    host = parsed.netloc
    path = parsed.path
    lower = url.lower()

    return {
        "url_len": len(url),
        "host_len": len(host),
        "path_len": len(path),
        "query_len": len(parsed.query),
        "dots": url.count("."),
        "hyphens": url.count("-"),
        "underscores": url.count("_"),
        "slashes": url.count("/"),
        "digits": sum(c.isdigit() for c in url),
        "letters": sum(c.isalpha() for c in url),
        "special_chars": len(re.findall(r"[@?&=%$#!~]", url)),
        "has_at": int("@" in url),
        "has_ip": int(bool(re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", ext.domain + "." + ext.suffix) or re.match(r"^\d{1,3}(\.\d{1,3}){3}", host))),
        "is_https": int(parsed.scheme == "https"),
        "subdomain_count": len(ext.subdomain.split(".")) if ext.subdomain else 0,
        "tld_len": len(ext.suffix),
        "domain_len": len(ext.domain),
        "suspicious_words": sum(w in lower for w in SUSPICIOUS_WORDS),
        "entropy": entropy(url),
        "digit_ratio": sum(c.isdigit() for c in url) / max(len(url), 1),
        "has_port": int(parsed.port is not None),
    }
