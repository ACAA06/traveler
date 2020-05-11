from flask import *
import locale
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = '8ffe05624dfe0efdf7c7f67288d4f4ce5005e0dfb6a1bc48366ef9906dd0586e'

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	if session['username'] is 'clement':
		return redirect(url_for('index'))
	else:
		return render_template('login.html',error="u haven't logged in")

@app.route('/login-page')
def login_page():

	if 'username' not in session or session['username'] == '':
		return render_template('login.html')
	else:
		return redirect(url_for('home'))


@app.route('/login', methods=['POST'])
def verify_credentials():
    name=request.form['login_username']
    password=request.form['login_password']
    session['username']=name
    if name=='clement'and password=='clem':
        return redirect(url_for('trip'))
    else:
        error='Incorrect username or password. Please try again.'
        return render_template('login.html',error=error)



@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('index'))

@app.route('/trip')
def trip():
	document_path = os.getcwd() +"\\trips.txt"
	print(document_path)
	file1=open(document_path,"a+")
	file1.seek(0)
	se=file1.readline()
	print(file1.readline())
	if(se==""):
		return render_template('create_activity.html',)
	else:
		file1.seek(0)
		lines = file1.readlines()
		list=[]
		#print(lines.split(";"))
		for line in lines:
			l=line.split(";")
			a={}
			print(l)
			a['name']=l[0]
			a['tname'] = l[1]
			a['start_time']=l[2]
			a['end_time']=l[3]
			a['date']=l[4]
			a['price']=l[5]
			list.append(a)
		return render_template('trip.html',items=list)


@app.route('/make-trip', methods=['POST', 'GET'])
def make_trip():
	return render_template('create_activity.html', )

@app.route('/create-trip', methods=['POST', 'GET'])
def create_trip():
	document_path = os.getcwd() + "\\trips.txt"
	print(document_path)
	file1 = open(document_path, "a+")
	print(file1.read())
	from_name = request.form['place_name']
	to_name=request.form['to_name']
	start_time = request.form['start_time']
	end_time = request.form['end_time']
	date = request.form['date']
	cost = request.form['cost']
	file1.write(from_name+";"+to_name+";"+start_time+";"+end_time+";"+date+";"+cost)
	file1.write("\n")
	file1.close()
	return redirect(url_for('trip'))


if __name__ == '__main__':
	app.run(debug=True)