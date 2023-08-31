#!/bin/bash
# script send DELETE request to URL passed as  first argument and displays the body of the response
curl -s "$1" -X DELETE
