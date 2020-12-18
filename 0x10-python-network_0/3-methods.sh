#!/bin/bash
# Display response script http methods.
curl -sI "$1" | grep Allow | cut --complement -d ' ' -f1
