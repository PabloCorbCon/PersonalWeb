#import Flask
from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
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
def main_page():

	return render_template('main.html', posts=posts)

if __name__ == '__main__':
	
	app.run(debug = True)