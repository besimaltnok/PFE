### commands

```python
import commands # Only linux system
from os import popen2

data = commands.getoutput("cd")
print(data)

stdin, stdout = popen2("dir")

print(stdin)
print(stdout)
```
