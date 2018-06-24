from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index1():
	print("Hello Everyone")
	return render_template("index1.html")