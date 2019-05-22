from app import app
from flask import render_template, redirect, url_for, request
from app.forms import RegisterForm

@app.route('/', methods= ['GET', 'POST'])
def home():
	form = RegisterForm()
	if (request.method == 'POST') and (form.validate_on_submit()):
		email = request.form['email']
		fullname = request.form['fullname']
		username = request.form['username']
		password = request.form['password']

		return redirect(url_for('explore'))
	else:
		return render_template('home.html', form = form)

@app.route('/explore', methods= ['GET'])
def explore():
	return "coming soon"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")