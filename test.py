from flask import Flask, request
app = Flask(__name__)

@app.route("/train")
def hello():
    return "Hello noisy train"
#    a, b = 0, 1
#    while b < 1000:
#        return b
#        a, b = b, a+b

@app.route("/goodbye")
def goodbye():
    return "Goodbye World!"

@app.route("/user/<username>")
def user(username):
    return 'Hello %s' % username

@app.route("/place")
def place():
	location = request.args.get('location', '')
	password = request.args.get('pass', '')
	return "Loc: %s + Pass: %s" % (location, password)

app.run(debug=True)



