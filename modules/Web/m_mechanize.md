### Mechanize modülü hakkında


+ Mechanize modülü ile bir siteye login süreci

```python
import mechanize, getpass

# Bir tarayıcı açıyoruz
br = mechanize.Browser()

# Giriş yapmak istediğimiz url adresini oluşturduğumuz tarayıcı ile açıyoruz
br.open(url)

# Gerekli login bilgileri kullanıcıdan alınır.
user  = raw_input("Username : ")
passw = getpass("Password   : ")

# Giriş için kullanacağımız form sayfanın kaynak kodundan bakılıp seçilir.
br.select_form(nr=1)

# Bilgiler forma işlenir.
br.form['user']  = user
br.form['passw'] = passw

# Son olarak form submit edilir.
br.submit()
```

