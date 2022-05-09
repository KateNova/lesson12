import logging

from flask import Blueprint, render_template, request
from .utills import get_posts, search_post

main_blueprint = Blueprint("main_blueprint", __name__, template_folder='templates')


# добавление роута для вью главной страницы
@main_blueprint.route("/")
def page_index():
    """
    return: отрисованный шаблон index.html
    """
    return render_template("index.html")


@main_blueprint.route("/search/")
def page_search():
    """
    return: отрисованный шаблон post_list.html, заполненный данными
    об отобранных постах и поисковым запросом пользователя
    """
    logging.info("Пользователь выполнил поиск")
    return render_template("post_list.html",
                           posts=search_post(get_posts(), request.args["s"]),
                           query=request.args["s"])
