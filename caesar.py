from string import ascii_letters

def encrypt(string, key):
    alpha = ascii_letters
    result = ''
    for i in string:
        if i not in alpha:
            result += i
        else:
            new_key = (alpha.index(i) + key) % len(alpha)
            result += alpha[new_key]
    return result
print(encrypt("siyamak", 3))




def decrypt(string, key):
    key *= -1
    return encrypt(string, key)
print(decrypt('vlBdpdn', 3))



def burt_force(string):
    alpha = ascii_letters
    key = 1
    result = ''
    brute_force_data = {}

    while key <= len(alpha):
        result = decrypt(string, key)
        brute_force_data[key] = result
        key +=1
    return brute_force_data
print(burt_force("vlBdpdn"))