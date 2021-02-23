import http.client
from numpy import random

conn = http.client.HTTPSConnection("api.mailgun.net")
code=random.randint(999999)
payload = "from=mailgun@sandboxbb982a75ac924997852a2e52acf7ad6b.mailgun.org&to=jsf75192@cuoly.com&subject=Code authentication&text=Code authentication: \n{}".format(code)
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Authorization': 'Basic YXBpOjM3N2U0ZWEwZjc2N2MyMzhlOTdlZGRkZjYwMzAxMzhkLTZlMGZkM2E0LTg2OWVmZmYy'
}
conn.request("POST", "/v3/sandboxbb982a75ac924997852a2e52acf7ad6b.mailgun.org/messages", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))