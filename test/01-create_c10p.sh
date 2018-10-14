endpoint=http://localhost:8080
echo $endpoint > endpoint.txt

# Get Token
token=$(./get_admin_token.sh)

# Set Key Name and value
key=c10p_$RANDOM
val="init"
echo -e "\n\nKey is: $endpoint/keys/$key - Value is: '$val'"

# Write Key
echo "WRITE key"
echo $val | curl -s -X PUT -d @- $endpoint/keys/$key -H "Authorization: Bearer $token" 

# Get Key

echo -e "\n\nGET key"
curl -s $endpoint/keys/$key -H "Authorization: Bearer $token"

# Create Route

echo -e "\nCreate route for key"
out=$(curl -s -X POST $endpoint/routes -d '{"key":"'$key'", "content_type":"application/json"}' -H "Authorization: Bearer $token")

r=$(echo $out | tr '"' "\n" | grep routes)

echo -e "\nGet key from route $endpoint$r\n"
curl $endpoint$r
echo -e "\n"

echo "### DONE ###"
echo "B9y Route: $(basename $r)"
echo "B9y Key: $key"

echo "$(basename $r)" > route.txt
echo "$key" > key.txt
