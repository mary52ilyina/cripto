import codecs

def attack_repeating_key_xor(ciphertext, keysize=None, score=None):
    from itertools import cycle

    def xor(enc, k):
        return ''.join(chr(ord(a) ^ k) for a in enc)

    def score_english(string):
        freq = dict()
        freq['a'] = 834
        freq['b'] = 154
        freq['c'] = 273
        freq['d'] = 414
        freq['e'] = 1260
        freq['f'] = 203
        freq['g'] = 192
        freq['h'] = 611
        freq['i'] = 671
        freq['j'] = 23
        freq['k'] = 87
        freq['l'] = 424
        freq['m'] = 253
        freq['n'] = 680
        freq['o'] = 770
        freq['p'] = 166
        freq['q'] = 9
        freq['r'] = 568
        freq['s'] = 611
        freq['t'] = 937
        freq['u'] = 285
        freq['v'] = 106
        freq['w'] = 234
        freq['x'] = 20
        freq['y'] = 204
        freq['z'] = 6
        freq[' '] = 2320

        ret = 0

        for c in string.lower():
            if c in freq:
                ret += freq[c]

        return ret

    if score is None:
        score = score_english

    if keysize is None:
        def hamming(x, y):
            assert(len(x) == len(y))

            def popcount(a):
                if a == 0:
                    return 0
                else:
                    return (a % 2) + popcount(a / 2)

            return sum(popcount(ord(a) ^ ord(b)) for a, b in zip(x, y))

        def norm_dist(keysize):
            numblocks = (len(ciphertext) / keysize)
            blocksum = 0
            for i in range(numblocks - 1):
                a = ciphertext[i * keysize: (i+1) * keysize]
                b = ciphertext[(i+1) * keysize: (i+2) * keysize]
                blocksum += hamming(a, b)
            blocksum /= float(numblocks)
            blocksum /= float(keysize)
            return blocksum

        keysize = min(range(2, min(40, len(ciphertext))), key=norm_dist)

    key = [None]*keysize

    for i in range(keysize):
        d = ciphertext[i::keysize]
        key[i] = max(range(256), key=lambda k: score(xor(d, k)))

    plaintext = ''.join(chr(ord(a) ^ b) for a, b in zip(ciphertext, cycle(key)))

    return plaintext

cipher = "1c41023f564b2a130824570e6b47046b521f3f5208201318245e0e6b40022643072e13183e51183f5a1f3e4702245d4b285a1b23561965133f2413192e571e28564b3f5b0e6b50042643072e4b023f4a4b24554b3f5b0238130425564b3c564b3c5a0727131e38564b245d0732131e3b430e39500a38564b27561f3f5619381f4b385c4b3f5b0e6b580e32401b2a500e6b5a186b5c05274a4b79054a6b67046b540e3f131f235a186b5c052e13192254033f130a3e470426521f22500a275f126b4a043e131c225f076b431924510a295f126b5d0e2e574b3f5c4b3e400e6b400426564b385c193f13042d130c2e5d0e3f5a086b52072c5c192247032613433c5b02285b4b3c5c1920560f6b47032e13092e401f6b5f0a38474b32560a391a476b40022646072a470e2f130a255d0e2a5f0225544b24414b2c410a2f5a0e25474b2f56182856053f1d4b185619225c1e385f1267131c395a1f2e13023f13192254033f13052444476b4a043e131c225f076b5d0e2e574b22474b3f5c4b2f56082243032e414b3f5b0e6b5d0e33474b245d0e6b52186b440e275f456b710e2a414b225d4b265a052f1f4b3f5b0e395689cbaa186b5d046b401b2a500e381d61";


print(attack_repeating_key_xor(codecs.decode(cipher, "hex")))