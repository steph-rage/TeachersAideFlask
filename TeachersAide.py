from flask import Flask, render_template, request

teachers_aide = Flask(__name__)


@teachers_aide.route('/', methods = ['GET', 'POST'])
def load_login_page():
	return render_template('Login_page.html', message = "testing")

@teachers_aide.route('/newprofile/', methods = ['GET', 'POST'])
def load_new_profile():
	return render_template('New_profile.html')

@teachers_aide.route('/testeditor/', methods = ['GET', 'POST'])
def load_test_editor():
	return render_template('Test_editor.html', current_tests = {})

@teachers_aide.route('/testeditor/new/', methods = ['GET', 'POST'])
def load_new_test():
	return render_template('New_test.html')

'''@teachers_aide.route('/', methods = ['GET', 'POST'])
def load_question_detail(self, url_info, user_profile):
	new_path = url_info[0:-1]
	new_path = ('/').join(new_path)
	test_name = parse.unquote_plus(url_info[-2])
	test = user_profile.tests[test_name]
	question_number = int(url_info[-1].split('question')[1].split('detail')[0])
	question = test.question_list[question_number - 1]
	answers = user_profile.tests[test_name].questions[question]
	correct_answer = answers[-1]
	correct_answer_index = test.answer_choices.index(correct_answer)
	template_vars = {
		'path': new_path,
		'question_number': question_number,
		'test_name': test_name,
		'question': question,
		'number_of_choices': test.choices,
		'answers': answers,
		'correct_answer_index': correct_answer_index,
	}

	with open('Templates/question_detail.html', 'r') as html_file:
		html = Template(html_file.read()).render(template_vars)
	self.wfile.write(bytes(html, 'utf8')) 

@teachers_aide.route('/', methods = ['GET', 'POST'])
def load_add_questions(self, url_info, test_name, user_profile):
	test = user_profile.tests[test_name]
	pretty_url_info_last = parse.unquote_plus(url_info[-1])
	test_name_url = self.path if pretty_url_info_last == test_name else self.path + '/' + test.url_name
	questions_with_numbers = []
	for question in test.questions:
		questions_with_numbers.append(question)
	number_of_questions = len(questions_with_numbers)
	path_to_editor = self.path.split('/')
	path_to_editor.pop()
	path_to_editor = ('/').join(path_to_editor)
	template_vars = {
		'test_name_url': test_name_url,
		'test_name': test_name,
		'number_of_choices': test.choices,
		'letters': test.answer_choices,
		'questions': test.question_list,
		'number_of_questions': len(test.question_list),
		'path': self.path,
		'path_to_editor': path_to_editor,
	}

	with open('Templates/Add_questions.html', 'r') as html_file:
		html = Template(html_file.read()).render(template_vars)
	self.wfile.write(bytes(html, 'utf8'))'''
