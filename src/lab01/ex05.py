fio = list(map(str, input('ФИО: ').split()))

k=0

for i in fio:
    k+=len(i)

print(f'Инициалы: {fio[0][0].upper()}{fio[1][0].upper()}{fio[2][0].upper()}.')
print(f'Длина (символов): {k + len(fio)-1}')