#import Flask
from flask import Flask, render_template, url_for

app = Flask(__name__)

projects = [
	{
		'title':'Stork',
		'short_description':'Online local files manager'
	},
	{
		'title':'project 2',
		'short_description':'project 2 description',
	},
	{
		'title':'project 3',
		'short_description':'project 3 description',
	},
]

@app.route('/')
def home():

	return render_template('main.html', projects=projects)

if __name__ == '__main__':
	
	app.run(debug = True)