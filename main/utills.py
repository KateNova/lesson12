import json
from json import JSONDecodeError


def get_posts():
    """
    return: список словарей, полученный из прочтения файла posts.json
    """
    # выполнение кода, если нет ошибок
    try:
        with open("posts.json", "r", encoding="utf-8") as f:
            posts = json.load(f)
        return posts
    # обработка ошибки, если файл json не обнаружен
    except FileNotFoundError:
        print("Файл не найден")
        # возврат пустого списка для избежания остановки основной прогаммы
        return []
    # обработка ошибки, если файл json не удается преобразовать
    except JSONDecodeError:
        print("Файл не удается преобразовать")
        return []

def search_post(posts, user_input):
    """
    param posts: список постов
    param user_input: текстовая строка
    return: список постов, составленный по вхождению строки в пост
    """
    posts_list = []
    for post in posts:
        if user_input.lower() in post["content"].lower():
            posts_list.append(post)
    return posts_list
