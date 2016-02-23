### FTPlib modülü hakkında

+ FTP Login

```python
from ftplib import FTP
domain = "localhost" 
ftp    = FTP(domain)
login  = ftp.login(user='username', passwd='password')

```

+ Login işleminden sonra FTP üzerinde işlem yapmak

```python
ftp.pwd()

ftp.mkd()

ftp.getwelcome()

ftp.retrlines('LIST')

ftp.quit()

ftp.close()


```
