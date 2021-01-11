#!/usr/bin/python3
""" Python Script display url and  X-Request-Id """
import requests
import sys

if __name__ == "__main__":
    print(requests.get(sys.argv[1]).headers.get('X-Request-Id'))
