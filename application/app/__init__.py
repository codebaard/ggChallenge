"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, request, render_template
import sys
import os


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import indexHandler
    app.register_blueprint(indexHandler.bp)
    app.add_url_rule('/', endpoint='index')

    from . import apiHandler
    app.register_blueprint(apiHandler.bp)

    from . import errorHandler as error
    app.register_error_handler(404, error.handle_404)
    app.register_error_handler(400, error.handle_400)

    return app
