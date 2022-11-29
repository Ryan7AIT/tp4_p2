from flask import Flask, render_template, request

app = Flask(__name__)


persons =  [
	{
		"nom" : "JOHN",
		"prenom" : "DOE",
		"points" : 15
	},
	{
		"nom" : "BOB",
		"prenom" : "CARLON",
		"points" : 9
	},

	{
		"nom" : "RAYANE",
		"prenom" : "SMITH",
		"points" : 13
	},

]


@app.route('/')
def index():
	return render_template('index.html')



@app.route('/personsData')
def doData():
	return render_template('persons_list.html', persons = persons)




if __name__ == "__main__":
	app.run(debug=True, port=5000)