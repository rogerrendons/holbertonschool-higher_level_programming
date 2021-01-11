#!/usr/bin/python3
""" Python Script fetch https://intranet.hbtn.io/status """
from urllib import request

if __name__ == '__main__':

    with request.urlopen('https://intranet.hbtn.io/status') as response:
        Cache = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(Cache)))
        print("\t- content: {}".format(Cache))
        print("\t- utf8 content: {}".format(Cache.decode('utf-8')))
