from Crypto.Util.number import *
s = "label"
for i in s:
    print(chr(ord(i)^13),end = '')