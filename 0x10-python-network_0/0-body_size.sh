#!/bin/bash
# Take URL show size body in the response
curl -sI "$1" | grep Content-Length | cut -d ' ' -f2
