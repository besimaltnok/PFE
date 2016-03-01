### Temel Bilgiler


+ Değişken tanımlama
```python
a = "besim"
b = 5
c = 8.3
a, b, c = "besim", 5, 8.3
```

+ Değişken olarak tnımlayamadıklarımız
```python
import keyword
listem = keyword.kwlist
```

+ Print() Fonksiyonu
```python
print("Ali")
print("Mehmet Köse", "Besim", "İsmail")
print("""Herkes için Python
Yayında ...""")

print("www", ""besimaltinok", "com", sep=".")
# www.besimaltinok.com

print("Besim", "Altinok", sep=None)
# Besim Altinok

f = open("file.txt", "w") 
print("Herkes için Python", file=f)
f.close()
```

+ Fonksiyon tanımlama
```python
def Fonksiyon():
    pass
```
