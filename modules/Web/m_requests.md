### Requests modülü hakkında ###

+ GET ve POST istekleri

```python
import requests
get  = requests.get(url)
post = requests.post(url)
```

+ İsteklere timeout değeri ekleme

```python
import requests
get  = requests.get(url,  timeout=0.01)
post = requests.post(url, timeout=0.008)
```
+ İsteklere parametre  ekleme

```python
import requests
payload = {'user': 'besim', 'passw': '1besim1'}
requests.get('http://url/giris', params=payload)
```

+ Status Code okuma

```python
get.status_code
```

+ Özel header alanı oluşturma (HTTP headers)

```python
headers = {'user-agent': 'mybrowser'}
requests.get(url, headers=headers)
```

+ HTTP response okuma

```python
resp  = requests.get(url)
resp.headers
resp['expires']
```

+ Dönen içeriği okuma

```python
get.getText()
```
### Yetkilendirme Süreci ###

+ Basic

```python
from requests.auth import HTTPBasicAuth
requests.get('https://url/login', auth=HTTPBasicAuth('user', 'pass'))
# veya #
requests.get('https://url/login', auth=('user', 'pass'))
```

+ Digest

```python
from requests.auth import HTTPDigestAuth
requests.get('https://url/login', auth=HTTPDigestAuth('user', 'pass'))
```
