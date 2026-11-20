import numpy as np
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')



def num_letters(num_rows,num_cols):
    return 2*num_rows + 2*num_cols - 4

rows = 0
for row in data:
    columns = len(row)
    rows+=1
print('Colums:',columns)
print('Rows:',rows)

print(num_letters(rows,columns))

letters = []

for i in data[0,:]:
    letters.append(str(i))
for i in data[1:,-1]:
    letters.append(str(i))
a = columns-2
for i in data[-1,:-1]:
    letters.append(str(data[-1,a]))
    a-=1
a = 2
for i in data[:-1,0]:
    letters.append(str(data[-a,0]))
    a+=1
print(letters)
a = 0
b = 0
words1 = []
words2 = []
for i in letters:
    try:
        words1.append(str(letters[a]+letters[a+1]))
        a+=1
    except:
        continue
a = -1
print(words1)
#bonus: all possible combinations
for i in letters:
    a += 1
    b = 0
    for j in letters:
        words2.append(str(letters[a]+letters[b]))
        b+=1
# vvv output here vvv remove # to see 
#print(words2)





'''
for i in data:
    for a in i:
        if len(a) == 0:
            continue
        else:
            letters.append(str(a))
'''
