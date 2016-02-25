### spwd modülü hakkında


```python
import spwd
p = spwd.getspnam(username)
print p
```
+ Dönen değer ve içerikleri

```python
0   sp_nam      : Login olmak için kullanılan kullanıcı ismi
1	sp_pwd      : Şifreli parola
2	sp_lstchg   : En son ne zaman değiştirildiği
3	sp_min      : Minimum değişim tarihi
4	sp_max      : Maximum değişim tarihi
5	sp_warn     : Şİfres süresü dolmadan kaç gün önce kullanıcı uyarılmalı
6	sp_inact    : Şifre süresi dolduktan kaç gün sonra kullanıcı hesabı bloke olacak
7	sp_expire   : Parolanın süresi
8	sp_flag     : Reserved
```
