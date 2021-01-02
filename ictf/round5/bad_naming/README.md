# Bad Naming

- **Description:** Timmy just learned python, but he isn't good at naming variables. Try to find out what the variable `important` is, and put it after `pastebin.com/` to get the flag.
- **Attachments:** https://fdownl.ga/D17B1002B7
- **Category:** Reversing/Crypto
- **Points:** 75

---

To solve this challenge, you must analyze a badly written Python file, which makes it quite hard to understand.

When script is run, it just displays a message saying that you failed:

``` shell
$ python 123.py
Disapointing...
```

The final check in the script is:

```python
if pip_important == "Ro[4OEC4[UV>":
    print("impressive!")
else:
    print("Disapointing...")
```

The `pip_important` variable must have a certain value. Following the data flow, it can be seen that `pip_important` is built in this loop:

```python
pip_important = ""
supa_strong = ""
for n in nothin_important:
  n = ord(n)
  n += 1
  n = chr(n)
  pip_important += n
```

Input data in this loop comes only from `nothin_important`. `nothing_important` is initialized in:

```python
nothin_important = important_tottaly.decode('ascii')
```

`important_tottaly` is assigned here:

```python
important_tottaly = base64.b64encode(randomvar)
```

Finally, `randomvar` is assigned here:

```python
important = ""
pip_important = "ictf{7h1s_f1@g_1s_1mp0r7an7_bu7_s@d1y_f@k3}"
import base64
randomvar = important.encode('ascii')
```

`randomvar` value depends on `important`, which is an empty string. The challenge consists hence in finding the correct value for `important` which, at the end of the program, will lead to a correct value for `pip_important`.

The script can be cleaned up:

- `pip_important`, which contains the fake flag shown above, is reassigned a few lines below. The fake flag value is never read and can be deleted.
- All the imports can be moved to the top of the file. `turtle` and `random` are imported but are never used. They can be safely deleted.
- `supa_strong` is never used and ca be deleted.

Here is the script after such cleanup. It is a bit more readable (see [123_cleanup.py](123_cleanup.py)):

```python
import base64

important = ""
randomvar = important.encode('ascii')
important_tottaly = base64.b64encode(randomvar)
nothin_important = important_tottaly.decode('ascii')
pip_important = ""
supa_strong = ""
for n in nothin_important:
  n = ord(n)
  n += 1
  n = chr(n)
  pip_important += n
if pip_important == "Ro[4OEC4[UV>":
    print("impressive!")
else:
    print("Disapointing...")
```

`important` is the input data, hence the flag. It is encoded into bytes, then encoded into base 64.

Now let's analyze the loop. Each character of the base 64 string is converted into an integer. This integer is increased, converted to a char and concatenated to `pip_important`.

The final value is "`Ro[4OEC4[UV>`". To retrieve the input value, one has to simply convert each character to an integer and subtract 1 from it. Finally, the output buffer has to be decoded from base 64:

```python
>>> import base64
>>> pip_important = "Ro[4OEC4[UV>"
>>> for i in range(len(pip_important)):
	out += chr(ord(pip_important[i]) - i)

	
>>> base64.b64decode(out)
b'Bvw40we5'
```

This gives us the Pastebin URL https://pastebin.com/Bvw40we5, which contains the flag.

Solution: ictf{n1c3_r3v3r\$1ng_\$k1lzzz}