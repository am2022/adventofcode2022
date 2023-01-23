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

max1 = 0
max2 = 0
max3 = 0

for j in num:
    if j > max1:
        max1 = j

num.remove(max1)

for j in num:
    if j > max2:
        max2 = j

num.remove(max2)

for j in num:
    if j > max3:
        max3 = j

num.remove(max3)

print(max1 + max2 + max3)