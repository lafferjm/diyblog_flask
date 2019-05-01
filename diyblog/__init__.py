from flask import Flask, redirect, url_for
from diyblog.config import Config


def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    from . import blog
    app.register_blueprint(blog.bp)

    @app.route('/')
    def index():
        return redirect(url_for('blog.index'))

    return app
