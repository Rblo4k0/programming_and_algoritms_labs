import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON-файл в CSV."""
    jp = Path(json_path)
    cp = Path(csv_path)

    if not jp.exists():
        raise FileNotFoundError("Указанный JSON файл не найден")

    if jp.suffix.lower() != ".json":
        raise ValueError("Указанный файл не формата JSON")

    try:
        with open(jp, encoding="utf-8") as p:
            data = json.load(p)
    except json.JSONDecodeError as e:
        raise ValueError(f"Пустой JSON или неподдерживаемая структура: {e}") from e

    if not isinstance(data, list) or not data:
        raise ValueError("Файл JSON пустой или имеет неправильный формат")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")

    # Сбор всех уникальных ключей для заголовка
    fieldnames = []
    for element in data:
        for key in element:
            if key not in fieldnames:
                fieldnames.append(key)

    cp.parent.mkdir(parents=True, exist_ok=True)
    with open(cp, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON (список словарей)."""
    cp = Path(csv_path)
    jp = Path(json_path)

    if not cp.exists():
        raise FileNotFoundError("Указанный CSV файл не найден")

    if cp.suffix.lower() != ".csv":
        raise ValueError("Указанный файл не формата CSV")

    with open(cp, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("Файл CSV пустой")
        data = list(reader)

    if not data:
        raise ValueError("Файл CSV не содержит данных")

    jp.parent.mkdir(parents=True, exist_ok=True)
    with open(jp, "w", encoding="utf-8") as p:
        json.dump(data, p, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")