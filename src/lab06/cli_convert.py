import argparse
from src.lab05.csv_xlsx import csv_to_xlsx
from src.lab05.json_csv import csv_to_json, json_to_csv


def main() -> None:
    """CLI-конвертеры данных для lab06."""
    parser = argparse.ArgumentParser(description="CLI-конвертеры данных для lab06")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p1 = subparsers.add_parser("json2csv", help="Перевод JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV файл")

    p2 = subparsers.add_parser("csv2json", help="Перевод CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON файл")

    p3 = subparsers.add_parser("csv2xlsx", help="Перевод CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX файл")

    args = parser.parse_args()

    if args.command == "json2csv":
        json_to_csv(args.input, args.output)
        print(f"Успешно сконвертировано в {args.output}")
    elif args.command == "csv2json":
        csv_to_json(args.input, args.output)
        print(f"Успешно сконвертировано в {args.output}")
    elif args.command == "csv2xlsx":
        csv_to_xlsx(args.input, args.output)
        print(f"Успешно сконвертировано в {args.output}")


if __name__ == "__main__":
    main()