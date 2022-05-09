import json
from json import JSONDecodeError


def add_post(post):
    """
    список словарей, полученный из прочтения файла posts.json
    """
    # выполнение кода без ошибок
    try:
        with open("posts.json", "r", encoding="utf-8") as f:
            posts = json.load(f)

        # добавление новой публикации в список словарей ("posts.json)
        posts.append(post)

        with open("posts.json", "w", encoding="utf-8") as f:
            json.dump(posts, f, ensure_ascii=False)
    # обработка ошибки при условии отсуствия файла json
    except FileNotFoundError:
        print("Файл не найден")
    # обработка ошибки, если файл json не удается преобразовать
    except JSONDecodeError:
        print("Файл не удается преобразовать")


class NotImageError(Exception):
    """
    создание класса для ошибки
    """
    pass
