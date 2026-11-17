from flask import Flask, request, render_template_string
from scan import scan

app = Flask(__name__)

PAGE = """
<!doctype html>
<title>URL Detector</title>
<style>
  body { font-family: sans-serif; max-width: 640px; margin: 40px auto; background: #111; color: #eee; }
  input[type=text] { width: 100%; padding: 10px; box-sizing: border-box; }
  button { margin-top: 10px; padding: 10px 20px; }
  .BENIGN { color: #4caf50; }
  .SUSPICIOUS { color: #ffb300; }
  .MALICIOUS { color: #f44336; }
</style>
<h2>AI-Powered Malicious URL Detector</h2>
<form method="post">
  <input type="text" name="url" placeholder="Enter a URL" value="{{ url or '' }}">
  <button type="submit">Scan</button>
</form>
{% if verdict %}
  <h3 class="{{ verdict }}">{{ verdict }} ({{ '%.1f' % (prob * 100) }}%)</h3>
  <p>Source: {{ src }}</p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    url = verdict = prob = src = None
    if request.method == "POST":
        url = request.form["url"].strip()
        if url:
            verdict, prob, src = scan(url)
    return render_template_string(PAGE, url=url, verdict=verdict, prob=prob, src=src)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
