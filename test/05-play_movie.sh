if [ "$#" != "1" ]
then
	echo -e "Need parameter: B9y key for the display\nExample: $0 c10p_554f03d700e043c2b900deced0f25871"
	exit
fi

key=$1

# Get Token
token=$(./get_admin_token.sh)
endpoint=$(cat endpoint.txt)

echo '{"type":"video","content":"http://blub.krash.net/videos/s.mp4","height":"0","width":"0"}' | curl -X PUT -d @- $endpoint/keys/$key -H "Authorization: Bearer $token"
