f = open("data.txt", "rt") #you should put you data file name instead of data.txt

buff = f.read()

b = []
num = []
buff_num = 0

b = buff.split("\n")

#print(list(b))

x = 0

for i in b:
    if i != '':
        buff_num += int(i)
    elif i == '':
        x += 1
        num.append(buff_num)
        buff_num = 0

#print(num)

max = 0

for j in num:
    if j > max:
        max = j

print(max)