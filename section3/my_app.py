from flask import Flask

app = Flask(__name__) # __name__ gives a file a unique name.

@app.route('/') # 'http://www.google.com/' - home page
def home():
	return 'Hello, world!'


app.run(port=5000)