<html>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script>
    var previous = null;
    var current = null;
    setInterval(function() {
        $.getJSON("/current", function(json) {
            current = JSON.stringify(json);
            if (previous && current && previous !== current) {
                console.log('refresh');
                location.reload();
            }
            previous = current;
        });
    }, 2000);
</script>
<body>
  {{ !render }}
</body>
</html>
