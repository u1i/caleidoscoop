from bottle import Bottle, request, view, response, redirect
import time, io, json, markdown2, requests, b9y, uuid
app = Bottle()
b9y = b9y.B9y()

#data_url = "http://localhost:8080/routes/573bb87e-25d5-4877-97b9-2ff440ecb22f"

def get_content(data_url):
	response = requests.request("GET", data_url)
	r = {}

	if response.text == 'init':
		r["type"] = "init"
		return(r)

	c=json.loads(response.text)

	r["type"] = c["type"]
	r["content"] = c["content"]
	r["width"] = c["width"]
	r["height"] = c["height"]
	return(r)

@app.get('/')
def root():
	return(dict(message="nothing here." + b9y.endpoint))

@app.get('/new')
@view('new')
def root():
	uu = str(uuid.uuid4())
	key = "c10p_" + uu.replace('-','')
	b9y.set(key,"init")
	route = b9y.create_route(key, 'application/json')
	id = route.replace('/routes/','')
	return(dict(url='/view/' + id, dataurl=b9y.endpoint + route, id=id, key=key))

@app.get('/view/<id>')
@view('dyn')
def do_view(id):
	out = "ready."
	dataurl = b9y.endpoint + "/routes/" + id

	try:
		c = get_content(dataurl)
	except:
	#out = "<h1>hello!</h2><br>Updated at: " + str(c) + " " + str(int(time.time()))
		out = "some error in the content."
		return(dict(render=out, url = dataurl))

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

	return(dict(render=out, url = dataurl))
