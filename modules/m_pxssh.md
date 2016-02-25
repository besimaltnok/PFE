
### pxssh modülü hakkında ###

+ Login

```python
import pxssh
import getpass
ssh   = pxssh.pxssh() 
host  = raw_input("Domain   :")
user  = raw_input("Username : ")
passw = getpass("Password   : ")
ssh.login(host, user, passw)
```
+ Login işleminden sonra komut çalıştırma

```python
command = "uptime" 
ssh.sendline(command)
```

+ çoklu komut çalıştırma

```python
c1 = "uptime" 
c2 = "ld"
ssh.sendline(c1;c2)
```
