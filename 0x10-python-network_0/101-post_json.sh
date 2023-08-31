#!/bin/bash
# Script sends JSON POST request to URL passed as first arg, and displays  body of  response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
