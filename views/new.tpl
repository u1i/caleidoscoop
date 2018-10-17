<html>
<body>
New display generated. ID is {{ id }}<br>&nbsp;<br>
View URL: <a href="{{ url }}">{{ url }}</a><br>&nbsp;<br>

Data URL: <a href="{{ dataurl }}">{{ dataurl }}</a><br>&nbsp;<br>
B9y Key: {{ key }}<br>&nbsp;<br>
<hr>

Example cURL command to update the display:<br>&nbsp;<br>

<code>curl -X PUT -d '{"type": "image","content": "http://blub.krash.net/katong.jpg","height": "0","width": "0"}' -H "Authorization: Bearer {{ token }}" http://localhost:8080/keys/{{ key }}</code>

</body>
</html>
