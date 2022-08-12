import json
from json import JSONDecodeError


def load_json(path: str) -> list[dict] | None:
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except JSONDecodeError:
            return None


def fill_db(table, data: list[dict], session) -> None:
    with session.begin():
        for item in data:
            session.add(table(**item))
