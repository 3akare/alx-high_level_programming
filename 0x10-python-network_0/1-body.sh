#!/bin/bash
# Takes in a URL, sends a GET request to the URL, and displays the body of the response
size=$(curl -sI ${1} | grep "HTTP/1.1" | cut -d " " -f2)
if [ $size -eq 200 ]
then
    curl -sI ${1}
fi