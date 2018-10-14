curl -X POST \
  http://localhost:8080/set \
  -H 'Cache-Control: no-cache' \
  -d '{"type":"video", "content":"http://blub.krash.net/videos/c.mp4", "width":"100", "height":"70"}'
