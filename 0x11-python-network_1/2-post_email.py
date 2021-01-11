#!/usr/bin/python3
""" Python Script Send POST Request """

if __name__ == "__main__":
    import sys
    from urllib import request, parse

    Mail = parse.urlencode({'email': sys.argv[2]})
    Mail = Mail.encode('utf-8')
    with request.urlopen(sys.argv[1], Mail) as response:
        Mail = response.read().decode('utf-8')
        print(Mail)
