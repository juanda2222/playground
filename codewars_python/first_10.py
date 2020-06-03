def square_digits(num):
    num_string = str(num)
    ret = list()
    for digit in num_string:
        ret.append(str(int(digit) ** 2))
    
    return int("".join(ret))

#print(square_digits(9119))

def is_isogram(string):
    lower_string = string.lower()
    tester_dic = dict()
    for letter in lower_string:
        try: 
            tester_dic[letter]
            return False
        except:
            tester_dic[letter] = True

    return True

# print(is_isogram("sdgWDsdf"))

from math import sqrt 

def is_square(n):    
    if n < 0:
        return False
    return sqrt(n) % 1 == 0

#print(is_square(4))

def find_short(s):
    # your code here
    words = s.split(" ")
    min_len = len(words[0])
    for word in words:
        if len(word) < min_len:
            min_len = len(word)

    return min_len

print(find_short("this is a set of words"))