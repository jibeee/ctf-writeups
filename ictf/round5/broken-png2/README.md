# broken-png2

- **Description:** Second problem for the Fix Broken PNG series.
- **Attachments:** https://fdownl.ga/9A891BA8FC
- **Category:** Forensics
- **Points:** 75

---

PNG header has been tampered: the magic value has been replaced with "GOODLUCK". Note also that an extra byte has been added:

```raw
00000000  47 4F 4F 44 4C 55 43 4B 00 00 00 00 0D 49 48 44  GOODLUCK.....IHD
```

becomes:

```raw
00000000  89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52  ‰PNG........IHDR
```

CRC for the PLTE chunck has been replaced with "HELO", and is hence invalid:

```shell
$ pngcheck broken2-fixed-header.png
broken2-fixed-header  CRC error in chunk PLTE (computed c78af170, expected 48454c4f)
ERROR: broken2-fixed-header
```

CRC32 can also be computed manually:

```python
>>> hex(zlib.crc32(bytes.fromhex("50 4C 54 45 FF A5 00 00 00 00 7F 52 00 5F 3D 00 DF 90 00 1F 14 00 3F 29 00 BF 7B 00 9F 67 00")))
'0xc78af170'
```

Finally, "IDAT" chunk has been renamed to "DWAT":

```shell
$ pngcheck broken2-fixed-header.png
broken2-fixed-header.png  illegal (unless recently approved) unknown, public chunk DWAT
ERROR: broken2-fixed-header.png
```

After having restored the chunk name, file can be opened. It contains the flag.

Solution : ictf{CRC_is_linear_over_XOR}
