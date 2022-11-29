from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('exo9.html')

@app.route('/result', methods=["GET"])
def doResult():
	maVal1 = request.args.get("vala")
	maVal2 = request.args.get("valb")
	maVal3 = request.args.get("valc")
	monResultat = int(maVal1) + int(maVal2) + int(maVal3)

	return render_template('exo9result.html', val1 = maVal1, val2 = maVal2, val3 = maVal3, result = monResultat)


if __name__ == "__main__":
	app.run(debug=True)