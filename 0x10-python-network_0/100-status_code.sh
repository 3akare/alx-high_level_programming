#!/bin/bash
# Sends a request to  aURL passed as an argument, and displays only the status code of the response
curl -sI "$1" | grep "HTTP/1.1" | cut -d " " -f2
