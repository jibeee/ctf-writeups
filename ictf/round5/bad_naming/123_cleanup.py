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


