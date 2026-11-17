from scan import scan

def test_allowlist():
    assert scan("https://www.google.com")[0] == "BENIGN"

def test_ip_login_flagged():
    assert scan("http://192.168.1.5/admin/login.php")[0] in ("SUSPICIOUS", "MALICIOUS")

def test_feed_hit():
    with open("data/openphish.txt") as f:
        url = f.readline().strip()
    assert scan(url)[0] == "MALICIOUS"

def test_malformed_url_does_not_crash():
    scan("http://[bad-url")
