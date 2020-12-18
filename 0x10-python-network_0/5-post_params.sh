#!/bin/bash
# Get URL sends POST request displays response
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
