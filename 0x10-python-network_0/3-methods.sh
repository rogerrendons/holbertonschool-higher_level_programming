#!/bin/bash
# Display response script http methods.
curl -sI "$1" | grep Allow | cut -d ' ' -f2
