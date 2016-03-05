### Temel Bilgiler


+ Değişken tanımlama
```python
a = "besim"
b = 5
c = 8.3
a, b, c = "besim", 5, 8.3
```

+ Değişken olarak tanımlayamadıklarımız
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

print("www", "besimaltinok", "com", sep=".")
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

### Dosya işlemleri

+ Dosya Okuma 1
```python
file = open("file.txt", "r")
data = file.read()
print data
file.close()
```
+ Dosya Okuma 2 (Satır Satır okuma)
```python
file = open("file.txt", "r")
data = file.readline()
print data
file.close()
```
+ Dosya Okuma 3 (liste şeklinde)
```python
file = open("file.txt", "r")
data = file.readlines()
print data
file.close()
```

+ Dosya Okuma (with open)
```python
with open("filename", "r") as dosya:
    print(filename.read())
```
+ Dosya Yazma 1
```pytho
file = open("file.txt", "w")
file.write("Merhaba Meryem")
file.close()
```

+ Dosya Yazma 2 
```pytho
file = open("file.txt", "a")
file.write("Merhaba Meryem")
file.close()
```
