f = open("data.txt", "rt") #you should put you data file name instead of data.txt

buff = f.read()

move = buff.split("\n")

#print(list(move))

score = 0

for i in move:
    if i[2] == 'X':
        score += 1
    elif i[2] == 'Y':
        score += 2
    elif i[2] == 'Z':
        score += 3

for j in move:
    if j[0] == 'A' and j[2] == 'X':
        score += 3
    elif j[0] == 'B' and j[2] == 'Y':
        score += 3
    elif j[0] == 'C' and j[2] == 'Z':
        score += 3

    elif j[0] == 'A' and j[2] == 'Y':
        score += 6
    elif j[0] == 'A' and j[2] == 'Z':
        score += 0

    elif j[0] == 'B' and j[2] == 'X':
        score += 0
    elif j[0] == 'B' and j[2] == 'Z':
        score += 6

    elif j[0] == 'C' and j[2] == 'X':
        score += 6
    elif j[0] == 'C' and j[2] == 'Y':
        score += 0

print(f"final score: {score}")
