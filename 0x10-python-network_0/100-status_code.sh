#!/bin/bash
# sends request to URL passed as arg, and displays onl status code of response
curl -so /dev/null -w "%{http_code}" "$1"
