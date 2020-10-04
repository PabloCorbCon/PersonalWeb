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
@app.errorhandler(404)
def error404(err=None):
	e = {
		'number':'404',
		'description':'We could not find the page you are looking for, perhaps you have misspelled the link or the page is private.' 
	}
	return render_template('error.html', title='404', error=e), 404

if __name__ == '__main__':
	app.run(debug =True, port=5000)