#!/bin/bash
# Request URL and show status response
curl -so /dev/null -w "%{http_code}" "$1"
