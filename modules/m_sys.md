### sys modülü hakkında


```python
import sys

sys.version # python version bilgisini alır.Örnek :
2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)]

sys.platform # pythonun çalıştığı sistemin platform ismini verir.

sys.version_info # bize bir demet döndürür.
sys.version_info(major=2, minor=7, micro=9, releaselevel=’final’, serial=0)

sys.argv # kullanıcıdan program için parametre alır.
sys.argv[1] # ikinci paramtre

sys.stdout.write(“BesimCo!\n”) 
# Ekrana çıktı verir.
print “type in value: “, ; sys.stdin.readline()[:-1] # Kullanıcıdan veri alır.

```
