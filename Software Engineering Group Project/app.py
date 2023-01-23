import logging
import socket
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from security_filter import SecurityFilter
from Resources.config import Disconnect

# Logging Setting
local_logging = logging.FileHandler('carbon.log', 'a')
local_logging.setLevel(logging.WARNING)
local_logging.addFilter(SecurityFilter())
formatter = logging.Formatter('%(asctime)s : %(message)s', '%m/%d/%y/%Y %I:%M:%S %p')
local_logging.setFormatter(formatter)
logger = logging.getLogger()
logger.propagate = False


app = Flask(__name__)

# Config of remote database
app.config.from_pyfile('Resources/config.py')
db = SQLAlchemy(app)


@app.route('/')
def index():
    """Render initial home page"""
    return render_template("index.html", hasNav=True)


# add error pages views
@app.errorhandler(400)
def page_bad_request(error):
    return render_template('400.html', hasNav=True), 400


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', hasNav=True), 404


@app.errorhandler(403)
def page_forbidden(error):
    return render_template('403.html', hasNav=True), 403


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', hasNav=True), 500


@app.errorhandler(503)
def service_unavailable(error):
    return render_template('503.html', hasNav=True), 503


if __name__ == "__main__":
    my_host = "127.0.0.1"
    free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    free_socket.bind((my_host, 0))
    free_socket.listen(5)
    free_port = free_socket.getsockname()[1]
    free_socket.close()

    # Import blueprints
    from calculator.views import calculator_blueprint
    from users.views import users_blueprint
    from quiz.views import quiz_blueprint
    from carbongram.views import carbongram_blueprint
    from information.views import information_blueprint
    from admin.views import admin_blueprint

    # Register blueprints to app
    app.register_blueprint(calculator_blueprint)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(quiz_blueprint)
    app.register_blueprint(carbongram_blueprint)
    app.register_blueprint(information_blueprint)
    app.register_blueprint(admin_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'users.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # add handler to logger
    logger.addHandler(local_logging)

    app.run(host=my_host, port=free_port, debug=True)

    Disconnect().shutdown()
