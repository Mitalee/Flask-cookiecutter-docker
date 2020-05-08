#!/usr/bin/env python

from flask import Flask, render_template, session, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy

from werkzeug.debug import DebuggedApplication



db = SQLAlchemy()


def create_app(main=True, debug=True):
    """Create an application."""
    app = Flask(__name__)
    app.config.from_object('config.settings')

    app.config['SECRET_KEY'] = 'secret!'

    
    from walletextension.blueprints.wallet import blog
    app.register_blueprint(blog)
    
    db.init_app(app)

    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)
    
    return app