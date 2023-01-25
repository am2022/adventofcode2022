f = open("data.txt", "rt") #you should put you data file name instead of data.txt

buff = f.read()

move = buff.split("\n")

#print(list(move))

score = 0

for j in move:
    if j[2] == 'X':
        if j[0] == 'A':
            score += 3
        elif j[0] == 'B':
            score += 1
        elif j[0] == 'C':
            score += 2

        score += 0
    elif j[2] == 'Y':
        if j[0] == 'A':
            score += 1
        elif j[0] == 'B':
            score += 2
        elif j[0] == 'C':
            score += 3

        score += 3
    elif j[2] == 'Z':
        if j[0] == 'A':
            score += 2
        elif j[0] == 'B':
            score += 3
        elif j[0] == 'C':
            score += 1

        score += 6
    else:
        print("error 2\n-----------------")

print(f"final score: {score}")