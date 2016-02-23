### FTPlib modülü hakkında

+ FTP Login

```python
from ftplib import FTP
domain = "localhost" 
ftp    = FTP(domain)
login  = ftp.login(user='username', passwd='password')

```
