def format_record(rec: tuple[str, str, float]) -> str:
    '''Функция форматирует запись, изменяя её вид

    Raises:
        TypeError:
            'На вход нужен кортеж'
        ValueError:
            'В кортеже должно быть 3 элемента'
            'ФИО введено не корректно'
            'Отсутствует группа'
    '''

    fio = []
    flag = 0

    if not isinstance(rec, tuple): raise TypeError('На вход нужен кортеж')

    if len(rec) != 3: raise ValueError('В кортеже должно быть 3 элемента')
    if len(rec[0].strip().split()) < 2 or len(rec[0].strip().split()) > 3: raise ValueError('ФИО введено не корректно')
    if not len(rec[1].strip()): raise ValueError('Отсутствует группа')

    for el in rec[0].strip('').split():
        if len(el) and flag:
            fio.append(el[0].upper() + '.')
            flag = 1

        if len(el) and not flag:
            fio.append(el[0].upper() + el[1:] + ' ')
            flag = 1

    return f'{''.join(fio)}, гр. {rec[1]}, GPA {rec[2]:.2f}'


print(f'''
("Иванов Иван Иванович", "BIVT-25", 4.6) -> {format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}
("Петров Пётр", "IKBO-12", 5.0) -> {format_record(("Петров Пётр", "IKBO-12", 5.0))}
("Петров Пётр Петрович", "IKBO-12", 5.0) -> {format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}
("  сидорова  анна   сергеевна ", "ABB-01", 3.999) -> {format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}
("Иванов Иван Иванович", "     ", 4.6) -> {format_record(("Иванов Иван Иванович", "    ", 4.1))}
''')
