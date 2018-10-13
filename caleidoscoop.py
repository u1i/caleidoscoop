from bottle import Bottle, request, view, response
import time, io, json, markdown2
app = Bottle()
datastore="/tmp/cldscp.dat"

@app.route('/set', method='POST')
def set_content():

	try:
		payload = json.load(request.body)
		ctype = payload["type"]
		content = payload["content"]
		width = payload["width"]
		height = payload["height"]
	except:
		response.status = 400
		return dict({"message":"No valid JSON found in post body or mandatory fields missing."})

	with io.open(datastore, 'w', encoding="utf-8") as outfile:
		outfile.write(unicode(request.body.read()))
	outfile.close()
	response.status = 201
	return dict({"message":"ok"})

def get_content():
	with io.open(datastore, mode='r', encoding='utf-8') as file_handle:
	    file_content = file_handle.read()
	file_handle.close()

	c=json.loads(file_content)

	r = {}
	r["type"] = c["type"]
	r["content"] = c["content"]
	r["width"] = c["width"]
	r["height"] = c["height"]
	return r

@app.get('/current')
def do_api():
#    try:
#        with io.open(datastore, mode='r', encoding='utf-8') as file_handle:
#            file_content = file_handle.read()
#        file_handle.close()
#    except:
#        response.status = 400
#        return dict({"message":"error"})
#
#    c=json.loads(file_content)

	c = get_content()
	return dict(c)

@app.get('/')
@view('dyn')
def do_templ():

	out = "ready."

	try:
		c = get_content()
	except:
	#out = "<h1>hello!</h2><br>Updated at: " + str(c) + " " + str(int(time.time()))
		out = "some error in the content."
		return(dict(render=out))

	if c["type"] == "video":
		out = '''<div align="center">
		<video width="1280" height="720" controls autoplay muted loop>
		  <source src="''' + c['content'] + '''" type="video/mp4">
		  Your browser does not support the video tag.
		</video>
		</div>'''

	if c["type"] == "image":
		out = "<div align='center'><img src='" + c['content'] + "' border='0'></div>"

	if c["type"] == "markdown":
		out = '<div style="color:white;">' + markdown2.markdown(c['content']) + '</div>'

	if c["type"] == "youtube":
		out = '''<div align="center">
	<iframe width="420" height="315"
	src="https://www.youtube.com/embed/''' + c['content'] + '''?autoplay=1&mute=1" frameborder="0">
	</iframe></div>'''

	return(dict(render=out))
