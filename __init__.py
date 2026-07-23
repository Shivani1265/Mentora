from flask import Flask
from flask_pymongo import PyMongo
from flask_login import LoginManager
from config import config
import os

mongo = PyMongo()
login_manager = LoginManager()

def create_app(config_name=None):
    """Application factory function"""
    if config_name is None:
        config_name = os.getenv('FLASK_ENV', 'development')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize extensions
    mongo.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    
    # Register blueprints
    from app.routes import auth, dashboard, messaging, ai_assistant, profile
    
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)
    app.register_blueprint(messaging.bp)
    app.register_blueprint(ai_assistant.bp)
    app.register_blueprint(profile.bp)
    
    # Create indexes
    with app.app_context():
        try:
            mongo.db.users.create_index('email', unique=True)
            mongo.db.messages.create_index([('sender_id', 1), ('receiver_id', 1)])
            mongo.db.connections.create_index([('student_id', 1), ('faculty_id', 1)], unique=True)
        except Exception as e:
            print(f"Index creation warning: {e}")
    
    return app
