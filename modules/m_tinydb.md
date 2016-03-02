### TinyDB!

+ Neden TinyDB

Kurulum gerektirmemesi
Kod ile birlikte taşınabilen bir veri tabanı olması
100% json
dosya tabanlı

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
