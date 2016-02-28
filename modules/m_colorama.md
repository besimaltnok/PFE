### colorama modülü hakkında 

+ Arkaplan ve yazı rengini değiştirme

```python
from colorama import Fore, Back, Style
print(Fore.RED + 'Text')
print(Back.GREEN + 'Text arkaplan')
print(Style.RESET_ALL)
print('Tekrar Normal')
```

+ Mevcut renkler 

```python
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
```
