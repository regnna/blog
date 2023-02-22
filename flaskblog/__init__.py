
from flask import Flask

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config

# app = Flask(__name__)


# app.config.from_object(Config)

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager=LoginManager()
login_manager.login_view='users.login'
login_manager.login_message_category='info'

# app.config['MAIL_USERNAME']=os.environ.get('EMAIL')
# app.config['MAIL_PASSWORD']=os.environ.get('PASS')

mail=Mail()


def create_App(config_clas=Config):
    app=Flask(__name__)
    Bootstrap(app)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    from flaskblog.users.routes import users
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    # Clear existing blueprints
    app.blueprints.clear()
    app.register_blueprint(users)
    # app.register_blueprint(posts)
    app.register_blueprint(main)
    # Register your new blueprint with the name 'posts'
    # app.register_blueprint(posts, name='posts')
    app.register_blueprint(posts, name='posts_v2')
    app.register_blueprint(errors)
    return app



