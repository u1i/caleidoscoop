while [ 1 ] 
do

curl -X POST \
  http://localhost:8080/set \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: caf0acaf-2e99-4a13-b95a-af98f9960d8d' \
  -d '{"type":"markdown","content":"Dynamic Markdown Example '''"$RANDOM"'''\n============\n\nParagraphs are separated by a blank line.\n\n2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists\nlook like:\n\n  * this one\n  * that one\n  * the other one\n\nNote that --- not considering the asterisk --- the actual text\ncontent starts at 4-columns in.\n\n> Block quotes are\n> written like so.\n>\n> They can span multiple paragraphs,\n> if you like.\n\nUse 3 dashes for an em-dash. Use 2 dashes for ranges (ex., '\''it'\''s all\nin chapters 12--14'\''). Three dots ... will be converted to an ellipsis.","height":"0","width":"0"}'

sleep 1
done
