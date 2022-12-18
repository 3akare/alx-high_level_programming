#!/bin/bash
# Sends a request to  aURL passed as an argument, and displays only the status code of the response. -w is the write out option. It writes out %{http_code}\n which is a special variable. For More check (https://everything.curl.dev/usingcurl/verbose/writeout)
curl -L "$1" -o /dev/null -w '%{http_code}\n' -s
