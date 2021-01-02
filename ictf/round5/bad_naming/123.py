important = ""
pip_important = "ictf{7h1s_f1@g_1s_1mp0r7an7_bu7_s@d1y_f@k3}"
import base64
randomvar = important.encode('ascii')
important_tottaly = base64.b64encode(randomvar)
import random
nothin_important = important_tottaly.decode('ascii')
import turtle
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


