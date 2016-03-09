### MySQLdb

+ Kurulumu
```python
sudo apt-get install python-mysqldb
```

+ Dahil etmek
```python
import MySQLdb
```

+ Veritabanı bağlantısı
```python
db = MySQLdb.connect("localhost","user","pass","DB_name" )
```

+ Sorgu çalıştırmak
```python
sql = "SORGU"
db.cursor()
cursor.execute(sql)
db.close()
```
