#!/bin/bash
# Script sends POST request and displays body response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
