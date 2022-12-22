#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, and display the body of the response.
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
