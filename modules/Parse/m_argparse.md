### Argparse modülü hakkında

+ Argüman tanımlama

```python
import argparse
parser = argparse.ArgumentParser("nmap handler", description)
parser.add_argument("--host", help="--host <hostname>", required=True)
parser.add_argument("--port", help="--port <port>", type=int, required=True)
args = parser.parse_args()
```

+ Tanımladığımız argümanların anlamı

```python
help     = Parametrenin kullanımı hakkında bilgi
type     = Kullanıcıdan alınacak parametrenin type bilgisi
required = Gerekli mi değil mi ?
```

+ Varsayılan bir değer tanımlamak istersek

```python
DEFAULT_PASS_LIST = "/home/pythoncu/pass.txt"
parser.add_argument("--passlist", "-p", help="wordlist for password, format:/home/user/passlist.txt", default=DEFAULT_PASS_LIST)
```

+ Tanımladığımız argümanı kullanabilmek için

```python
hostname = args.host
port     = args.port
```
