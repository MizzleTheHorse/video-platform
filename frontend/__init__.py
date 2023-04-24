# init.py
from flask import Flask
from .models import User
from .user_client import UserClient
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    client = UserClient()

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SESSION_REFRESH_EACH_REQUEST'] = False

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        #query user here
        try:
            id = int(user_id)
            response = client.get_user_by_id(user_id=id)
        except Exception as e:
            response = False
        if response:
            user = User(response.user_id, response.name, response.email, response.hashed_password)
            return user
        else:
            return None
    
    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    # todo: Refactor blueprint main to register other modules 
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for 
    from .content import content as content_blueprint
    app.register_blueprint(content_blueprint)

    return app