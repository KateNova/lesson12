import logging

from flask import Blueprint, render_template, request
from .utills import add_post, NotImageError

# создание экземпляра класса Blueprint loader_blueprint
loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder='templates')


# добавление роута для вью страницы, отвечающей за создание новой публикации
@loader_blueprint.route("/post", methods=["GET", "POST"])
def page_post_form():
    # возврат формы клиенту по методу GET
    if request.method == "GET":
        return render_template("post_form.html")
    # обработка полученных из формы данных
    elif request.method == "POST":
        try:
            # получение картинки из формы по ключу
            picture = request.files["picture"]
            # обработка ошибки типа загруженной картинки
            if picture.filename.split(".")[-1] not in ["jpg", "jpeg", "png"]:
                # добавление логирования, если картинка не нужного расширения
                logging.info("Файл не принадлежит к типу 'jpeg' и 'png'")
                # вызов ошибки, связанной с типом картинки
                raise NotImageError("Файл не принадлежит к типу 'jpeg' и 'png'")
            # получение текста поста из формы по ключу
            content = request.form["content"]
            # сохранение картинки в папку "uploads"
            picture.save(f"./uploads/{picture.filename}")
            # создание словаря для дальнейшего добавления в существующий список словарей "posts.json"
            post = {"pic": f"/uploads/{picture.filename}", "content": content}
            add_post(post)
            return render_template("post_uploaded.html", post=post)
        except NotImageError:
            return "Файл не принадлежит к типу 'jpeg' и 'png'"
        # выполнение кода в случае возникновения ошибок
        except Exception as e:
            logging.error('Ошибка загрузки')
            return f"ошибка загрузки"
