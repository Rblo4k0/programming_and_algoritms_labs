count = 1
n = int(input(f'in_{count}: '))

k=0

for _ in range(n):
    count+=1
    sp = list(map(str, input(f'in_{count}: ').split()))
    if sp[-1] == 'True':
        k += 1

print(f'out: {k}, {n-k}')