# Get Token
token=$(./get_admin_token.sh)
key=$(cat key.txt)
endpoint=$(cat endpoint.txt)

echo '{"type":"image","content":"http://blub.krash.net/mistakes.png","height":"0","width":"0"}' | curl -X PUT -d @- $endpoint/keys/$key -H "Authorization: Bearer $token"
