# Tells python that this is a packge
# Flaskr will be the applicaiton Factory

import os

from flask import Flask

def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flask.sqlite'),
    )

    if test_config is None:
        # Load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:1
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    @app.route('/hello')
    def hello():
        return 'Hello World!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from .import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

# Stoped at https://flask.palletsprojects.com/en/2.3.x/tutorial/install/