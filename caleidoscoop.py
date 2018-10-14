from bottle import Bottle, request, view, response
import time, io, json, markdown2, requests
app = Bottle()
data_url = "http://localhost:8080/routes/573bb87e-25d5-4877-97b9-2ff440ecb22f"

def get_content():
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
@view('dyn')
def do_templ():
	out = "ready."

	try:
		c = get_content()
	except:
	#out = "<h1>hello!</h2><br>Updated at: " + str(c) + " " + str(int(time.time()))
		out = "some error in the content."
		return(dict(render=out, url = data_url))

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

	if c["type"] == "init":
		out = '<div style="color:white;">Caleidoscoop ready.</div>'

	if c["type"] == "youtube":
		out = '''<div align="center">
	<iframe width="420" height="315"
	src="https://www.youtube.com/embed/''' + c['content'] + '''?autoplay=1&mute=1" frameborder="0">
	</iframe></div>'''

	return(dict(render=out, url = data_url))
