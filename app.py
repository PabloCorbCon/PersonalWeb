#import Flask
from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')
	
@app.route('/contact')
def contact():
	return render_template('contact.html', title='contact', cards=[2, 3, 4, 5, 6])

if __name__ == '__main__':
	app.run(debug =True, port=5000)