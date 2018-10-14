if [ "$#" != "1" ]
then
	echo -e "Need parameter: B9y key for the display\nExample: $0 c10p_554f03d700e043c2b900deced0f25871"
	exit
fi

key=$1

# Get Token
token=$(./get_admin_token.sh)
endpoint=$(cat endpoint.txt)

curl -X PUT -d '{"type":"youtube","content":"HZrsuEWw9m8","height":"0","width":"0"}' $endpoint/keys/$key -H "Authorization: Bearer $token"
