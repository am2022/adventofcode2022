import string

f = open("data.txt", "rt") #you should put you data file name instead of data.txt
o = open("data.txt", "rt") #you should put you data file name instead of data.txt

buff = f.read()

move = buff.split("\n")

chars = []

score = 0

ascii_chars = string.ascii_letters

for i in range(0, int(len(move) / 3)):
    if i == 298:
        break

    elf1 = o.readline()
    elf2 = o.readline()
    elf3 = o.readline()

    for j in ascii_chars:
        if j in elf1 and j in elf2 and j in elf3:
            chars.append(j)

for i in chars:
    for j in ascii_chars:
        if i == j:
            score += ascii_chars.index(i) + 1

print(f"final score is {score}")
