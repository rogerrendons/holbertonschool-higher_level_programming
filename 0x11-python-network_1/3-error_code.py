#!/usr/bin/python3
""" Script sends a request to URL and displays
the body of the response (decoded in utf-8) """

if __name__ == "__main__":
    import urllib
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as resp:
            print(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
