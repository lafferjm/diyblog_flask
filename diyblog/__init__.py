from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from diyblog.config import Config

db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)

    from . import blog
    app.register_blueprint(blog.bp)

    @app.route('/')
    def index():
        return redirect(url_for('blog.index'))

    return app
