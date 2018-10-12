curl -X POST \
  http://localhost:8080/set \
  -H 'Cache-Control: no-cache' \
  -d '{"type":"video", "content":"http://techslides.com/demos/sample-videos/small.mp4", "width":"100", "height":"70"}'
