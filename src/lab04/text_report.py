import sys
from pathlib import Path

from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import count_freq, tokenize, top_n


def parse_cli_args():
    """Разбирает аргументы sys.argv для поддержки флагов --in и --encoding."""
    args = sys.argv[1:]
    input_paths = []
    encoding = "utf-8"

    i = 0
    while i < len(args):
        arg = args[i]
        if arg == "--encoding":
            if i + 1 < len(args):
                encoding = args[i + 1]
                i += 2
            else:
                print("ошибка: не указано значение для --encoding", file=sys.stderr)
                sys.exit(1)
        elif arg == "--in":
            i += 1
            # Считываем все пути после флага --in до следующего флага
            while i < len(args) and not args[i].startswith("--"):
                input_paths.append(Path(args[i]))
                i += 1
        elif not arg.startswith("--"):
            # Обычные позиционные аргументы без флагов
            input_paths.append(Path(arg))
            i += 1
        else:
            i += 1

    # Значения по умолчанию, если файлы не были переданы через аргументы
    if not input_paths:
        default_file = Path("data/lab04/input.txt")
        if default_file.exists():
            input_paths = [default_file]
        else:
            input_paths = sorted(Path("data/lab04").glob("*.txt"))

    return input_paths, encoding


def main():
    input_paths, encoding = parse_cli_args()

    if not input_paths:
        print("ошибка: нет файлов для обработки", file=sys.stderr)
        sys.exit(1)

    all_tokens = []
    per_file_rows = []

    # 1. Чтение всех файлов с учётом переданной кодировки
    for path in input_paths:
        text = read_text(path, encoding=encoding)
        tokens = [t.casefold() for t in tokenize(text)]
        all_tokens.extend(tokens)

        # Данные для report_per_file.csv (топ-10 по каждому файлу)
        file_freq = count_freq(tokens)
        for word, count in top_n(file_freq, 10):
            per_file_rows.append((path.name, word, count))

    # 2. Общая статистика по всем файлам
    total_freq = count_freq(all_tokens)
    top_words = top_n(total_freq, 100)

    # 3. Сохранение отчетов в CSV
    out_csv = Path("data/lab04/report.csv")
    write_csv(top_words, out_csv, header=["word", "count"])

    write_csv(
        per_file_rows,
        "data/lab04/report_per_file.csv",
        header=["file", "word", "count"],
    )

    # Вывод результатов в консоль (stdout)
    files_str = ", ".join(p.name for p in input_paths)
    print(f"Обработано файлов ({len(input_paths)}): {files_str}")
    print(f"Кодировка: {encoding}")
    print(f"Всего слов: {len(all_tokens)}")
    print(f"Уникальных слов: {len(total_freq)}")
    print("Топ-5 слов:")
    for word, count in top_words[:5]:
        print(f"  {word}: {count}")
    print(f"Отчет сохранен в: {out_csv}")


if __name__ == "__main__":
    main()