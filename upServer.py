import os
import sqlalchemy
import string
import oauth2client
import httplib2
from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from datetime import datetime
import sys

import json
import requests
import codecs
from datetime import datetime
from datetime import date
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, asc, desc
from flask import session as sessionmaker
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from random import randint
from flask import make_response
import requests
from werkzeug.utils import secure_filename

from flask_login import LoginManager
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask_mail import Mail, Message
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
app = Flask(__name__)
app.secret_key = 'super_secret_key'

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_db_up import Base, User, UserMixin, Image



engine = create_engine('sqlite:///up.db')

Base.metadata.bind = engine

session = scoped_session(sessionmaker(bind = engine))

UPLOAD_FOLDER = os.path.dirname ('static/im/usrs/')

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
ALLOWED_EXTENSIONS_BOOKS = set(['pdf','epub','txt','epdf'])
ALLOWED_EXTENSIONS_VIDEOS = set(['mpg','mpeg','mp4','mov'])


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config.update(
    DEBUG=False,
    SESSION_COOKIE_SECURE=True,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE='Lax',
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = '',
    MAIL_PASSWORD = ''
    )


mail = Mail(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"

@login_manager.user_loader
def load_user(id):
    user = session.query(User).filter_by(id = id).one()
    return user



@app.teardown_request
def remove_session(ex=None):
    session.remove()

@app.route('/logout')
def logout():
    print("logged out")
    logout_user()
    
    return redirect(url_for('home'))



@app.route('/', methods = ["GET","POST"])
def home():
	return render_template('index.html')




if __name__ == '__main__':

    app.debug = True

    app.run(host='0.0.0.0')

    # connect_args=={'check_same_thread': False}
