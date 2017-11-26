# sandbox/__init__.py

from flask import Flask

from picam.server.main.views import main_blueprint

app = Flask(
    __name__,
    template_folder='client/templates',
    static_folder='client/static'
)


app.register_blueprint(main_blueprint)
