# #!/usr/bin/python3
# """ Python Script Send POST Request """

if __name__ == "__main__":
    import sys
    from urllib import request, parse
    mail = parse.urlencode({'email': sys.argv[2]})
    mail = mail.encode('utf-8')
    with request.urlopen(sys.argv[1], mail) as response:
            mail = response.read().decode('utf-8')
            print(mail)
