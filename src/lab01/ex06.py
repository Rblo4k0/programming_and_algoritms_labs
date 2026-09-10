n = int(input())

k=0

for _ in range(n):
    sp = list(map(str, input().split()))
    if sp[-1] == 'True':
        k += 1

print(k, n-k)