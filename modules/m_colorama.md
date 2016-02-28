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

### ANSI color code (Terminal renklendirme)

+ Söz dizimi 

```python
print "\033[5;41;32mGREEN TEXT\033[0m" 

START_SEQx;y;zmDISPLAY_TEXTEND_SEQ

Starting sequence: \033[
x;y;z: ANSI color codes
Display text: Text you want to display
Ending sequence: \033[0m
```

