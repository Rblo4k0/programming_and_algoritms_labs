st = input()

fst_ind = -1
sec_ind = -1
numbers = '0123456789'

for i in range(len(st)-1):
    if st[i].isupper():
        fst_ind = i
    if st[i] in numbers:
        sec_ind = i+1
        break

step = sec_ind - fst_ind
for i in range(fst_ind, len(st), step):
    print(st[i], end='')
