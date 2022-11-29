from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('exo10.html')

@app.route('/result', methods=["POST"])
def doResult():
	maVal1 = request.form["vala"]
	maVal2 = request.form["valb"]
	maVal3 = request.form["valc"]
	maVal4 = request.form["vald"]

	monResultat = ((int(maVal1) + int(maVal2)) * int(maVal3)) / int(maVal4)

	return render_template('exo10result.html', val1 = maVal1, val2 = maVal2, val3 = maVal3, val4 = maVal4, result = monResultat)

	# return render_template('exo10result.html', val1 = maVal1, val2 = maVal2, val3 = maVal3, val4 = maVal4, result = 11)



if __name__ == "__main__":
	app.run(debug=True)