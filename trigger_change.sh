# change the value in the cURL command

curl -X POST \
  http://localhost:8080/set \
  -H 'Cache-Control: no-cache' \
  -d '{"url":"test3"}'
