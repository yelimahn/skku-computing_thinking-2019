def string_input():
    return input("please enter your countable list:")

def count_string(s):
    d=dict()
    for char in s:
        if char not in d:
            d[char]=1;
        else:
            d[char]=d[char]+1

    return d

s=string_input()
d=count_string(s)
print(d)
