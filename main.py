import requests
import shutil
url= ""

filename = url.split("/")[-1]
r = requests.get(url, stream = True)
if r.status_code == 200:
    r.raw.decode_content = True
    with open(filename,'wb') as f:
        shutil.copyfileobj(r.raw, f)   