from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from diyblog.config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)
    
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    db.init_app(app)
    migrate.init_app(app, db)

    from . import blog
    app.register_blueprint(blog.bp)

    @app.route('/')
    def index():
        return redirect(url_for('blog.index'))

    return app
