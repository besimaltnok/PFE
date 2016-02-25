### pefile modülü hakkında

+ Dosya analizi

```python
import pefile
pe = pefile.PE('/root/Desktop/l.exe')
is_dll  = pe.is_dll()
is_exe  = pe.is_exe()

```

+ Önemli örnekler

```python

def ImportTables():
	for entry in pe.DIRECTORY_ENTRY_IMPORT:
		dll.append(entry.dll)
		for import_list in entry.imports:
			import_table.append(import_list.name)

```

+ Önemli örnekler

```python

def Is_Packed():
	global is_packed
	if 'LoadLibraryA' in import_table:
		is_packed = 'True'
	else:
		is_packed = 'False'

```
