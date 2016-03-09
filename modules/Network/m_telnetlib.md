### Telnetlib modülü hakkında

+ Telnet ile login süreci

```python
from telnetlib import Telnet
import getpass

host = "domain"
user  = raw_input("Username : ")
passw = getpass("Password   : ") 

login = Telnet(host)
login.read_until("login: ")
login.write(user + "\n")

login.read_until("Password: ")
login.write(passw + "\n")

```

