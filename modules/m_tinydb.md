### TinyDB!

+ Neden TinyDB

```python
Kurulum gerektirmemesi
Kod ile birlikte taşınabilen bir veri tabanı olması
100% json
dosya tabanlı
```
+ Neden TinyDB değil

```python
Saniyede binlerce sorgu yapılacaksa performansı düşük kalır
```

+ Kurulumu

```python
pip install tinydb
```

+ import
```python
from tinydb import TinyDB, Query
db = TinyDB('db.json')
```

+ Sorgu nesnesi oluşturma
```python
sorgu = Query()
```

+ Eleman Ekleme
```python
db.insert({'type': 'armut', 'count': 7})
```
+ Eleman Arama
```python
db.searh(sorgu.type == 'armut')
```
+ Eleman Güncelleme
```python
db.update({'count': 10}, sorgu.type == 'armut')
```
+ Eleman Silme
```python
db.remove(sorgu.type == 'armut')
```
+ Eklenen Elemanları Çağırmak
```python
db.all()
db.all()[2]
db.all()[2]['type']
```
