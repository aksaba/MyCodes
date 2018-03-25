
import requests

url = "http://www.chennaimetrowater.tn.nic.in/public/lake.htm"
payload = {'frm2':'19/03/2018'}
r = requests.post(url,payload)
#with open("requests_results.html", "w") as f:
 #   f.write(r.content)
print r
