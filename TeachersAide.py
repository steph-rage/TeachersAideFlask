from flask import Flask, render_template, request

teachers_aide = Flask(__name__)


@teachers_aide.route('/', methods = ['GET', 'POST'])
def load_login_page():
	return render_template('Login_page.html', message = "testing")