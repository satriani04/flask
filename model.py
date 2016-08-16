from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:win@localhost/flask'
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(100))
	email = db.Column(db.String(100),unique=True)
	password = db.Column(db.String(100))
	posts = db.relationship('Post',backref='user',lazy='dynamic')
	
	def __repr__(self):
		return '<User %r>' % self.name


class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(100))
	body = db.Column(db.Text())
	user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Post %r>' % self.title

if __name__ == '__main__':
	manager.run()
