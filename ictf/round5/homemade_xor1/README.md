# homemade-xor1

- **Description:** Several people complained about my last homemade XOR. So here is one with full recipe (flag is redacted). Provided in attachments are the recipe in C and the result of `./xorr > homemade1.txt`
- **Attachments:**

https://s1.fdownl.ga/38DF789CE6-xorr.c
https://s1.fdownl.ga/855BA0E6F6-homemade1.txt

- **Category:** Reversing/Crypto

- **Points:** 100

---

A small program in C xor a flag with two keys. The most important function in the code is:

```c
char* getRandom(char ptxt[], char rand[], int iv)
{
    for (int i = 0; i < iv; ++i)
    {
        ptxt = getXOR(ptxt, rand);
    }
    return ptxt;
}
```

It xors two strings a given number of time. Note that any buffer xored with itself leads to a null buffer (as $0 \oplus 0 = 1 \oplus 1 = 0$). Hence, in the above code:

- `ptxt` will be equal to `ptxt` ^ `rand` if `iv` is odd.
- `ptxt` will not be changed if `iv` is even.

Here is the snippet that encrypts the flag (in `key3`):

```c
char* pass1 = getRandom(key1, key2, 5);
char* pass2 = getRandom(key1, key3, 3);
char* pass3 = getRandom(key1, key2, 7);
char* pass4 = getRandom(key1, key3, 2);
```

Code can be simplified as:

```
output = key1 ^ key2
output = output ^ key3
output = output ^ key2
```

Last statement has no effect, as 2 is even: `getRandom(key1, key3, 2)` will compute `key1 ^ key3 ^ key3 = key1 ^ (key3 ^ key3) = key1`.

Finally we get

`output = key1 ^ key2 ^ key3 ^ key2 = key1 ^ key3`

We can then retrieve the flag by computing: `key3 = ciphertext ^ key1`.

```python
>>> ct = bytes.fromhex("0E 0D 01 4B 08 0C 42 1B 31 56 46 72 1A 40 41 05 30 5F 18 13 5D 1B 16 5D 2B 4C 0A 0B 31 34 18 4C 5F 16 1C 34 1C 58 18 58 42 0A")
>>> key1 = b"gnu-strings-is-convenient-dont-you-think?"
>>> bytes([key1[i] ^ ct[i] for i in range(41)])
b'ictf{x0r_15_s3lf_1nv3rs3_and_@550c1@t1v3}'
```

Solution: ictf{x0r_15_s3lf_1nv3rs3_and_@550c1@t1v3}