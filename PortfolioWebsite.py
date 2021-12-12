from flask import Flask, render_template

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

if __name__ == "__main__":
	app.run(debug=True)