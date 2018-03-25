import requests

url = "http://duckduckgo.com/html"
payload = {'q':'x'}
r = requests.post(url, payload)
with open("requests_results.html", "w") as f:
    f.write(r.content)
