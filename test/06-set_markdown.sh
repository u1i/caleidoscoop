if [ "$#" != "1" ]
then
	echo -e "Need parameter: B9y key for the display\nExample: $0 c10p_554f03d700e043c2b900deced0f25871"
	exit
fi

key=$1

# Get Token
token=$(./get_admin_token.sh)
endpoint=$(cat endpoint.txt)

curl -X PUT -d '{"type":"markdown","content":"Markdown Example\n============\n\nParagraphs are separated by a blank line.\n\n2nd paragraph. *Italic*, **bold**, and `monospace`. Itemized lists\nlook like:\n\n  * this one\n  * that one\n  * the other one\n\nNote that --- not considering the asterisk --- the actual text\ncontent starts at 4-columns in.\n\n> Block quotes are\n> written like so.\n>\n> They can span multiple paragraphs,\n> if you like.\n\nUse 3 dashes for an em-dash. Use 2 dashes for ranges (ex., '\''it'\''s all\nin chapters 12--14'\''). Three dots ... will be converted to an ellipsis.","height":"0","width":"0"}' $endpoint/keys/$key -H "Authorization: Bearer $token"
