import csv
import sys
from pathlib import Path


def read_text(path, encoding="utf-8"):
    """Считывает текстовый файл по пути path.

    При отсутствии файла выводит сообщение в sys.stderr и завершает
    программу с кодом 1.
    """
    try:
        with open(path, encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"ошибка: файл не найден: {path}", file=sys.stderr)
        sys.exit(1)


def write_csv(rows, path, header=None, encoding="utf-8"):
    """Записывает данные rows в CSV-файл с кодировкой utf-8 и newline=""."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with open(p, "w", encoding=encoding, newline="") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)