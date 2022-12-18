#!/bin/bash
# Sends a request to a URL passed as an argument, and displays only the status code of the response. -w is the write out option. It writes out %{http_code}\n which is a special variable. For More special variables check (https://everything.curl.dev/usingcurl/verbose/writeout)
curl -sLw "%{http_code}" -o /dev/null "$1"
