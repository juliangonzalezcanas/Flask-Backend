from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from sqlalchemy import create_engine

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.run(port = 3000, debug=True)
    
    db.init_app(app)
    migrate.init_app(app, db)
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    
    with app.app_context():
        db.create_all()

    from app.routes import main
    app.register_blueprint(main)

    return app
