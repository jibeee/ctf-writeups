# batmans-cipherkick

- **Description:** Don't worry it is not a RSA challenge, although similar. You just have to figure out exactly which crypto technique it is, there are no twists: should be easy to implement.
- **Attachments:** https://fdownl.ga/481C2B902F
- **Category:** Crypto
- **Points:** 75

---

The attachment is a text files which contains two values: N, and a ciphertext. Both are big numbers.

My first try was to attempt to factor N, to see if it is prime or if it has small factors. Description of the challenges says it is "similar" to RSA. N seems indeed like a RSA modulus, a product of two primes, as factoring tools do not find a small factor.

N is only 512 bits. That means it can be factored with NFS, for example with [cado-nfs](http://cado-nfs.gforge.inria.fr/). As this challenge is worth only 75 points, there is probably another method. Actually, the factors or N are on [factordb](http://factordb.com/):

$N = p \times q$, with:

- $p = 109397118167414659469854315698685280846395418815987835066487939223142947575863$
- $q = 75867404082230064535529769847035529139210898256190940050437960991947122945007$

Now, the cipher. As there is no public exponent, like for RSA, algorithm is definitely a public key algorithm with a fixed exponent. The name of the challenge is a big hint: who is Batman's friend? Robin. I already knew the Rabin cipher, but if you don't know it, you can search, for example, for "robin public key cipher". First result is [Rabin cryptosystem](https://en.wikipedia.org/wiki/Rabin_cryptosystem).

Let $n$ be a product of two primes $p$ and $q$, and $m$ the message to encrypt.

Rabin's encryption is simply: $c=m^2 \mod n$.

Decryption is a bit more complicated:

1. First, compute the square roots of $c$ modulo $p$ and $q$, $m_p$ and $m_q$.
2. Then find $y_p$ and $y_q$ such as $y_p p + y_q q= 1$ using the extended Euclidian algorithm.
3. Finally, use the Chinese remainder theorem to find the four square roots of $c \mod N$.

There are 4 possible plaintext messages for a given ciphertext. The correct one is, for this challenge, the only one that is a printable string.

To solve the challenge, I used a [Python implementation](https://github.com/duckbill360/Rabin-Public-Key-Cryptosystem) of the cipher. It has to be adapted as this implementation adds a padding value to the message to be encrypted, to determine which of the 4 possible plaintexts is correct. For this challenge, the correct plaintext is the only one which contains a printable string.

Solution: ictf{Bez0ut5_c03ff1c1ent5?3xtended_3ucl1d_ftw}