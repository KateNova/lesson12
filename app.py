from flask import Flask, send_from_directory

# import and registration blueprint from package main and loader
from main.views import main_blueprint
from loader.views import loader_blueprint


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
