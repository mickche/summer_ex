# Exercise 15: Count Character Frequencies

def count_elems(text):
    counter = {}
    for elem in text:
        if elem in counter:
            counter[elem] += 1
        else:
             counter[elem] = 1
    return counter

print(count_elems("hello world"))


#2 

# text = "hello world"

# freq = {}
# for char in text:
#     freq[char] = freq.get(char, 0) + 1

# print(freq)