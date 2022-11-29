from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index8.html')

@app.route('/experience')
def experience():
	return render_template('experience.html')

@app.route('/centers_interet')
def centers_interet():
	return render_template('centers_interet.html')

if __name__ == "__main__":
	app.run(debug=True)