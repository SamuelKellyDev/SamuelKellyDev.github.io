from flask import Flask, render_template
# Flask is entirely for back-end, it doesn't replace JavaScript. 
app = Flask(__name__)
# TextArea tag defines a multi-line text input control. The textarea element is often used in a form to collect user inputs like comments or reviews.
@app.route("/")
def home():
	return render_template("index.html")

@app.route("/aboutme")
def aboutme():
	return render_template("aboutme.html")

@app.route("/contact") 
def contact():
	return render_template("contact.html")

@app.route("/game") 
def game():
	return render_template("game.html")

if __name__ == "__main__":
	app.run(debug=True)