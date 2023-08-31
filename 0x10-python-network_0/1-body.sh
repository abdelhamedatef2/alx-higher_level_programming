#!/bin/bash
#script takes  URL, sends  GET request and displays only  body of a 200 status code response
curl -Ls "$1"
