from flask import Flask, render_template, request, session, redirect, escape, url_for

import sqlite3

#from Test_creator import Test
#from Profile_creator import TeacherProfile

teachers_aide = Flask(__name__)

#Once working, will need to add cookies, and verification at each step.
#Add in a redirect to login page if no logged in user
#Need a way of storing profiles - start with json? Or straight use a database

profiles = sqlite3.connect('profiles.db')
profiles.execute('CREATE TABLE IF NOT EXISTS profile_info (USERNAME TEXT, PASSWORD TEXT)')

@teachers_aide.route('/', methods = ['GET', 'POST'])
def load_login_page(message = ""):
	if request.method == "POST":
		return render_template('New_profile.html')
	return render_template('Login_page.html', message = message)


@teachers_aide.route('/newprofile/', methods = ['GET', 'POST'])
def load_new_profile():
	return render_template('New_profile.html')


@teachers_aide.route('/<username>/testeditor/', methods = ['GET', 'POST'])
def load_test_editor(username):
	#Find profile in stored information
	return render_template('Test_editor.html', current_tests = {})


@teachers_aide.route('/login', methods = ['GET', 'POST'])
def load_logging_in():

	if request.method == 'POST':
		username = request.form["username"]
		password = unicode(request.form["password"])
		user_info = profiles.execute("SELECT PASSWORD FROM profile_info WHERE USERNAME == ?", (username,)).fetchone()
		print(user_info)
		print(user_info[0])
		if user_info[0] == password:
			return redirect(url_for("load_test_editor", username = username))

		else:
			return redirect(url_for("load_login_page", message = "That password was incorrect; please try again"))


@teachers_aide.route('/new_login', methods = ['GET', 'POST'])
def load_new_logging_in():

	if request.method == 'POST':
		username = request.form["username"]
		password = request.form["password"]
		profiles.execute("INSERT INTO profile_info VALUES (?, ?)", (username, password))
		return redirect(url_for("load_test_editor", username = username))

'''@teachers_aide.route('/<username>/testeditor/new/', methods = ['GET', 'POST'])
def load_new_test(username):
	return render_template('New_test.html')

@teachers_aide.route('/testeditor/<test_name>', methods = ['GET', 'POST'])
def load_add_questions(test_name):
	return render_template("Add_questions.html",
		test_name_url = test_name_url,
		test_name = test_name,
		number_of_choices = test.choices,
		letters = test.answer_choices,
		questions = test.question_list,
		number_of_questions = len(test.question_list),
		)


@teachers_aide.route('/testeditor/<test_name>/question<question_number>', methods = ['GET', 'POST'])
def load_question_detail(test_name, question_number):
	return render_template("question_detail.html", 
		question_number = question_number,
		test_name = test_name,
		question = question,
		number_of_choices = test.choices,
		answers = answers,
		correct_answer_index = correct_answer_index,
	)

 
'''