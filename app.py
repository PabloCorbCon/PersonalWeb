#import Flask
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/')
def home():
	"""
	This is the main function of the flask page,
	it uses the render_template() function to return the
	home.html HTML template.

	:parameters None:
	"""
	icons = [
		{
			'url':'https://twitter.com/pablocorbcon',
			'alt':'twitter',
			'route':'twitter'
		},
		{
			'url':'https://github.com/PabloCorbCon',
			'alt':'github',
			'route':'github'
		},
		{
			'url':'https://www.youtube.com/channel/UCYawvF7GUx2eo2QUbtfdtAg',
			'alt':'youtube',
			'route':'youtube'
		},
		{
			'url':'https://t.me/pablocorbcon',
			'alt':'telegram',
			'route':'telegram'
		}
	]
	return render_template('home.html', icons=icons)

@app.route('/app')
def application():
    return render_template('app.html')

@app.route('/error')
def error():
	"""
	There is not an specific error page, this route redirects to
	the home page
	"""
	return redirect(url_for('home'))

@app.route('/error/400')
@app.errorhandler(400)
def error400(err=None):
	"""
	This handler error function is used to
	create custom 400 error templates.
	It uses the @app.errorhandler() decorator
	to handle the error itself.
	"""
	e = {
		'number':'400',
		'description':'The request that this page has received is not valid. Perhaps your browser has been confused or you are using the wrong method to access this page.'
	}
	return render_template('error.html', title='400', error=e), 400

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
		'description':'We are sorry but you do not have authorization to access this page.'
	}
	return render_template('error.html', title='401', error=e), 401

@app.route('/error/403')
@app.errorhandler(403)
def error403(err=None):
	"""
	This handler error function is used to
	create custom 403 error templates.
	It uses the @app.errorhandler() decorator
	to handle the error itself.
	"""
	e = {
		'number':'403',
		'description':'We are sorry but access to this page is prohibited. Contact an administrator to grant you access.'
	}
	return render_template('error.html', title='403', error=e), 403

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

@app.route('/error/500')
@app.errorhandler(500)
def error500(err=None):
	"""
	This handler error function is used to
	create custom 500 error templates.
	It uses the @app.errorhandler() decorator
	to handle the error itself.
	"""
	e = {
		'number':'500',
		'description':'Do not worry, this error is not your fault. There has been an internal error on our server. We are trying to fix it.'
	}
	return render_template('error.html', title='500', error=e), 500


if __name__ == '__main__':
	app.run(debug=1, port=5000)
