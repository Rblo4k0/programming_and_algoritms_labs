import argparse
from pathlib import Path
from src.lib.text import count_freq, normalize, tokenize, top_n


def main() -> None:
    """CLI-утилита для вывода содержимого файла (cat) и анализа частоты слов (stats)."""
    parser = argparse.ArgumentParser(description="CLI-утилиты для lab06")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество отображаемых слов в топе",)

    args = parser.parse_args()
    path = Path(args.input)

    if args.command == "cat":
        if not path.exists():
            raise FileNotFoundError(f"Нет файла по указанному пути: {path}")

        with open(path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                if args.n:
                    print(f"{i:>4}\t{line}", end="")
                else:
                    print(line, end="")

    elif args.command == "stats":
        if args.top < 0:
            raise ValueError("Топ не может быть отрицательным")
        if not path.exists():
            raise FileNotFoundError(f"Нет файла по указанному пути: {path}")

        with open(path, "r", encoding="utf-8") as f:
            data = f.read()

        normal_text = normalize(data)
        tokens = tokenize(normal_text)
        words_cnt = count_freq(tokens)
        top_words = top_n(words_cnt, args.top)

        if top_words:
            max_len = max(max(len(word[0]) for word in top_words), len("слово"))
        else:
            max_len = len("слово")

        head = f"{'слово':<{max_len}} | частота"
        print(head)
        print("-" * len(head))
        for word, count in top_words:
            print(f"{word:<{max_len}} | {count}")


if __name__ == "__main__":
    main()