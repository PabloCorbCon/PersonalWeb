#import Flask
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
	"""
	This is the main function of the flask page,
	it uses the render_template() function to return the
	home.html HTML template.

	:parameters None:
	"""
	return render_template('home.html')
	
@app.route('/contact')
def contact():
	"""
	This is the contact page of the app, it uses the
	render_template() function to return the contacts.html
	HTML template.
	"""
	return render_template('contact.html', title='contact', cards=[2, 3, 4, 5, 6])

@app.route('/error/401')
@app.errorhandler(401)
def error401(err=None):
	"""
	This handler error function is used to
	create custom 401 error templates.
	It uses the @app.errorhandler() decorator
	to handle the error itself.
	"""
	e = {
		'number':'401',
		'description':'We are sorry but you do not have authorization to access this page' 
	}
	return render_template('error.html', title='401', error=e), 401

@app.route('/error/404')
@app.errorhandler(404)
def error404(err=None):
	"""
	This handler error function is used to
	create custom 404 error templates.
	It uses the @app.errorhandler() decorator
	to handle the error itself.
	"""
	e = {
		'number':'404',
		'description':'We could not find the page you are looking for, perhaps you have misspelled the link or the page is private.' 
	}
	return render_template('error.html', title='404', error=e), 404





if __name__ == '__main__':
	app.run(debug =True, port=5000)