#!/bin/bash
# script that takes in URL as an argument sends a GET request to the URL, and displays the body of the response
curl -sH "X-School-User-Id: 89" "$1"
