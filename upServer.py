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

from create_db_up import Base, User, UserMixin, Image,Cmts



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

login_manager.login_view = "home"

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
	print('home')
	return render_template('index.html')


@app.route('/su', methods = ["GET","POST"])
def upsignUp():
	print('in sign up')
	users = session.query(User).all()
	if request.method == 'POST':
		for u in users:
			print('checking if user in system already exists')
			if u.email.lower() == request.form['email'].lower():
				return redirect(url_for('home'))

		newUser = User(username = request.form['usr'], email = request.form['email'].lower())
		if request.form['p_word'] == request.form['p_word2']:

			newUser.p = request.form['p_word']
			session.add(newUser)
			session.commit()
			os.makedirs('static/im/usrs/' + str(newUser.id))
			print('user has been created')
			login_user(newUser, remember=True)
			return redirect(url_for('main',user = current_user.username))

		else:
			print('passwords do not match')
			return redirect(url_for('home'))



	return redirect(url_for('home'))


@app.route('/si', methods = ["GET","POST"])
def sifUsr():
	users = session.query(User).all()
	if request.method == 'POST':
		for u in users:
			if u.email.lower() == request.form['email']:
				if u.p == request.form['p_word']:
					login_user(u, remember=True)
					return redirect(url_for('main', user = u))
				return redirect(url_for('home'))

		return redirect(url_for('home'))
	return redirect(url_for('home'))



@app.route('/<string:user>')
@login_required
def main(user):
	thisUser = session.query(User).filter_by(id = current_user.id).one()
	userImages = session.query(Image).filter_by(user_id = current_user.id).all()
	cmts = session.query(Cmts).all()

	return render_template('main.html',cmts = cmts, folder = str(thisUser.id), user = thisUser, userImages = userImages)


# photoUploads

@app.route('/upload/', methods = ['GET','POST'])
@login_required
def upload_photo():
	userinfo = session.query(User).filter_by(id = current_user.id).one()
	allphotos = session.query(Image).filter_by(user_id = current_user.id).all()
	if request.method == 'POST':
		print('inside upload photo request')
		# check if the post requiest has the file part included
		if 'file' not in request.files:
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			path = 'static/im/usrs/' + str(userinfo.id)
			print(path)
			UPLOAD_FOLDER = os.path.dirname ('static/im/usrs/' + str(userinfo.id) + '/')
			app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
			for a in allphotos:
				if a.path == filename:
					filename = filename + str("1")
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			newPhoto = Image(path = filename, user_id = userinfo.id, img_desc = request.form['desc'])
			session.add(newPhoto)
			session.commit()
			print('photo added and saved')
			return redirect(url_for('main',user = current_user.username))
		return redirect(url_for('main',user = current_user.username))
	return redirect(url_for('main',user = current_user.username))










if __name__ == '__main__':

    app.debug = True

    app.run(host='0.0.0.0')

    # connect_args=={'check_same_thread': False}
