

def score(text):
    charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,.'\n"
    p = 0
    for s in text:
        if s in charset or s == ' ' or s == '\'':
            p += 1
    return p


# function that performs XOR operation on two strings
def xor(s1, s2):
    res = ""
    for i in range(0, len(s1)):
        res += chr(ord(s1[i]) ^ ord(s2[i % len(s2)]))

    return res


def main():
    _string = """]|d3gaj3r3avcvrgz}t>xvj3K\A3pzc{va=3V=t=3zg3`{|f.w3grxv3r3`gaz}t31{v..|3d|a.w13r}w?3tzev}3g{v3xvj3z`31xvj1?3k|a3g{v3uza`g3.vggva31{13dzg{31x1?3g{v}3k|a31v13dzg{31v1?3g{v}31.13dzg{31j1?3r}w3g{v}3k|a3}vkg3p{ra31.13dzg{31x13rtrz}?3g{v}31|13dzg{31v13r}w3`|3|}=3J|f3~rj3f`v3z}wvk3|u3p|z}pzwv}pv?3[r~~z}t3wz`gr}pv?3Xr`z`xz3vkr~z}rgz|}?3`grgz`gzpr.3gv`g`3|a3d{rgveva3~vg{|w3j|f3uvv.3d|f.w3`{|d3g{v3qv`g3av`f.g="""
    best = ""
    b = 0
    # brutforcing all possible values
    for i in range(1, 256):
        c = xor(_string, chr(i))
        if score(c) > b:
            b = score(c)
            best = c

    print("Plaintext: {}".format(best))


if __name__ == "__main__":
    main()
