### Requests modülü hakkında ###

+ GET ve POST istekleri

```python
import requests
get  = requests.get(url)
post = requests.post(url)
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
get.text
```
