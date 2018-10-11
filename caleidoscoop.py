from bottle import Bottle, request, view, response
import time, io, json
app = Bottle()
datastore="/tmp/cldscp.dat"

@app.get('/')
def get_home():

	return("this is caleidoscoop.")

@app.route('/set', method='POST')
def set_url():

    with io.open(datastore, 'w', encoding="utf-8") as outfile:
        outfile.write(unicode(request.body.read()))
    outfile.close()

    response.status = 201
    return dict({"message":"ok"})

@app.get('/api')
def do_api():

	return(dict(msg="hello!"))

@app.get('/current')
def do_api():
    try:
        with io.open(datastore, mode='r', encoding='utf-8') as file_handle:
            file_content = file_handle.read()
        file_handle.close()
    except:
        response.status = 404
        return dict({"message":"ID not found"})

    this_atm=json.loads(file_content)

    return dict(this_atm)

@app.get('/dynamic')
@view('dyn')
def do_templ():
	return(dict(message="hello! " + str(int(time.time()))))
