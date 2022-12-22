#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept.. -w is the write out option. It writes out %{http_code}\n which is a special variable. For More special variables check (https://everything.curl.dev/usingcurl/verbose/writeout)
curl -sI "$1" | grep "Allow" | cut -d " "  -f2-
