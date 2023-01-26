import string

f = open("data.txt", "rt") #you should put you data file name instead of data.txt

buff = f.read()

move = buff.split("\n")

chars = []

score = 0

ascii_chars = string.ascii_letters

for i in move:
    length = len(i)
    a = i[0:int(length / 2)]
    b = i[int(length / 2):]

    for j in ascii_chars:
        if j in a and j in b:
            chars.append(j)

for i in chars:
    for j in ascii_chars:
        if i == j:
            score += ascii_chars.index(i) + 1
            print(ascii_chars.index(i) + 1)

print(f"final score is {score}")
