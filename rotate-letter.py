
"""
("hello", 2) => "llohe"
("hello", 5) => "hello"
("hello", 7) => "llohe"
("hello", 6) => "elloh"
"""

def rotate(string, key):
    double_string = string + string
    if key <= len(string):
        return double_string[key:key + len(string)]
    else:
        return double_string[key - len(string):key]

print(rotate("hello", 12))

