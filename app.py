from flask import Flask, render_template, request, redirect, url_for, session, abort
from model import User, db
import bcrypt

app = Flask(__name__)
app.secret_key = 'donttellanyone'

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		#print(request)
		nama = request.form['nama'] 
		email = request.form['email'] 
		password = request.form['password'].encode('utf-8') 
		new_user = User(name=nama,email=email,password=bcrypt.hashpw(password, bcrypt.gensalt()))
		db.session.add(new_user)
		db.session.commit()
		session["is_login"] = True
		session["nama"] = nama
		return redirect(url_for('dashboard'))
	return render_template("register.html")

@app.route('/login',methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form['email'].encode('utf-8')
		password = request.form['password'].encode('utf-8')

		user_exist = User.query.filter_by(email=email).first()

		if user_exist is not None:
			if user_exist.password.encode('utf-8') == bcrypt.hashpw(password, user_exist.password.encode('utf-8')):
				session["is_login"] = True
				session["nama"] = user_exist.name
				return redirect(url_for('dashboard'))
			else:
				return "password salah"
			return "user ga ada"
		return "username dan password salah"				

	return render_template('login.html')		

@app.route("/dashboard")
def dashboard():
	if not session.get("nama"):
		return redirect(url_for('login'))
	return render_template("dashboard.html",user=session["nama"]) 	

@app.route("/logout")
def logout():
	session.pop('is_login', None)
	session.pop('nama', None)
	return redirect(url_for('index'))	


if __name__ == "__main__":
	app.run(debug=True)
