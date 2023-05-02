import os

from flask import Flask, render_template

from config import Config
from app.extensions.database import db
from flask_migrate import Migrate


def create_app(config_class=Config):
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate = Migrate(app, db)

    #  Register blueprints here
    from app.home import bp as main_bp
    app.register_blueprint(main_bp)

    from app.create_ki_thi import bp as create_ki_thi_bp
    app.register_blueprint(create_ki_thi_bp, url_prefix='/ki-thi')

    from app.qr_exam import bp as qr_exam_bp
    app.register_blueprint(qr_exam_bp, url_prefix='/qr-exam')

    from app.exam_score_collection import bp as exam_score_collection_bp
    app.register_blueprint(exam_score_collection_bp, url_prefix='/result')

    from app.find_info_sv import bp as find_info_sv_bp
    app.register_blueprint(find_info_sv_bp, url_prefix='/search-sv')

    return app
