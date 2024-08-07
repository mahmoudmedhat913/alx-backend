#!/usr/bin/env python3
"""task 0 basic Flask app"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """config class"""

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """retrieve the loacle for web page

    Return:
        str: best match
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """default route

    Return:
        html: homepage
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
