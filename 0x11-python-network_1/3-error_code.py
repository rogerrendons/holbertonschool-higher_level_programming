#!/usr/bin/python3
""" Write a Python script that takes in a URL, sends a
request to the URL and displays the body of the
response (decoded in utf-8)."""

if __name__ == "__main__":
    import sys
    from urllib import request, parse, error

    try:
        with request.urlopen(sys.argv[1]) as response:
            url = response.read().decode('utf-8')
            print(url)
    except error.HTTPError as errorurl:
            print("Error code: {}".format(errorurl.code))
