from bottle import Bottle, request, view
import time
app = Bottle()

@app.get('/')
def get_home():

	return("hello!")

@app.get('/api')
def do_api():

	return(dict(msg="hello!"))

@app.get('/dynamic')
@view('dyn')
def do_templ():
	return(dict(message="hello! " + str(int(time.time()))))
