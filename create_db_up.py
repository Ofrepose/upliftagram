import sys
import os
import sqlalchemy
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime, BigInteger
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_login import UserMixin

Base = declarative_base()

class User(UserMixin, Base):
	__tablename__ = 'user'

	id = Column(
		Integer, primary_key = True)

	name_first = Column(
		String(80))

	name_last = Column(
		String(80))

	username = Column(
		String(80))

	p = Column(
		String(80), nullable = False)

	email = Column(
		String(180), nullable = False)

	follow = Column(
		Text())

	follwers = Column(
		Text())

	bio = Column(
		Text())

	profile_picture = Column(
		String(150))


class Image(Base):
	__tablename__ = 'image'

	path = Column(
		String(150), nullable = False)

	id = Column(
		Integer, primary_key = True)

	user_id = Column(
		Integer, ForeignKey('user.id'))
	 
	user = relationship (User)

	heart_tot = Column(
		Integer, default = 0)

	laugh_tot = Column(
		Integer, default = 0)

	cry_tot = Column(
		Integer, default = 0)

	heart_usrs = Column(
		Text())

	laugh_usrs = Column(
		Text())

	cry_usrs = Column(
		Text())

	img_desc = Column(
		Text())

	# cmt_tot = Column(
	# 	Integer, default = 0)

class Cmts(Base):
	__tablename__ = 'cmts'

	id = Column(
		Integer, primary_key = True)

	img_id = Column(
		Integer, ForeignKey('image.id'))

	image = relationship(Image)

	cmt_owner = Column(
		Integer, ForeignKey('user.id'))

	user = relationship(User)	

	cmt = Column(
		Text())







engine = create_engine('sqlite:///up.db')
Base.metadata.create_all(engine)