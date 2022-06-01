import random

class OneTime:
    def encrypt(self, text):
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1,100)
            key.append(k)
            c = (i + k) * k
            cipher.append(c)
        print(cipher, key)


    def decrypt(self, chiper, key):
        plain = []
        for i in range(len(key)):
            p = int((chiper[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))
        result = "".join([i for i in plain])
        print(result)



on = OneTime()
on.encrypt("siyamak")
on.decrypt([17000, 16704, 15800, 2478, 6930, 17388, 8694], [85, 87, 79, 21, 45, 92, 54])
