#import Flask
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/contact')
def contact():
	return render_template('contact.html', title='contact', cards=[2, 3, 4, 5, 6])

@app.route('/error/404')
@app.errorhandler(404):
def error404():
	e = {
		'title':'Page not found',
		'number':'404',
		'description':'This page does not exist or it is a private page.<br>Check that you typed the link in the correct way.' 
	}
	return render_template('error.html', title='404', error=e)

if __name__ == '__main__':
	app.run(debug =True, port=5000)