import prime


def decryption(a, p, q):
    n = p * q
    r, s = 0, 0
    # find sqrt
    # for p
    if p % 4 == 3:
        r = prime.sqrt_p_3_mod_4(a, p)
    elif p % 8 == 5:
        r = prime.sqrt_p_5_mod_8(a, p)
    # for q
    if q % 4 == 3:
        s = prime.sqrt_p_3_mod_4(a, q)
    elif q % 8 == 5:
        s = prime.sqrt_p_5_mod_8(a, q)

    gcd, c, d = prime.egcd(p, q)
    x = (r * d * q + s * c * p) % n
    y = (r * d * q - s * c * p) % n
    lst = [x, n - x, y, n - y]

    return [p.to_bytes((p.bit_length() + 7) // 8, "big") for p in lst]


def main():
    n = 8299675369438719692429346867124546707751640425816191732040675610043554481287075447992524087489203341094226350053164998077984358117605583398826976109566041
    p = 109397118167414659469854315698685280846395418815987835066487939223142947575863
    q = n // p
    assert p * q == n

    ciphertext = 7393133392978435017631606326669002945645049245575327455199891934940471127163421964825217371440398090013070393620687586475550331584874262094419639415630197
    candidates = decryption(ciphertext, p, q)
    for plaintext in candidates:
        if plaintext.startswith(b"ictf{"):
            print(plaintext.decode())


if __name__ == "__main__":
    main()
