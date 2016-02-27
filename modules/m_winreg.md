### _winreg modülü hakkında

+ Regedit üzerinde işlem yapmanızı sağlayan bir modüldür.


+ Regedit üzerinde okuma işlemi için

```python
import _winreg
key  = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run")
```

+ Regedit üzerinde yazma işlemi için

```python
import _winreg
key  = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run")
```
+ Kullanılabilecek diğer metotlar
