from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "<h1> Bienvenu sue Exercice 6 </h1>"

if __name__ == "__main__":
	app.run(debug=True,port = 8080)