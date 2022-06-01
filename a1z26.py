def encode(plain):
    return [ord(elm) - 92 for elm in plain]
print(encode("siyamak"))


def decode(encode):
    return ("".join(chr(elm + 92) for elm in encode))

print(decode([23, 13, 29, 5, 17, 5, 15]))