#!/usr/bin/python3
""" Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails” """

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit()

    result = requests.get("https://api.github.com/repos/{}/{}/commits".
                          format(sys.argv[2], sys.argv[1]))
    res = result.json()

for x in range(10):
    print("{}: {}".format(res[x].get("sha"), res[x].
          get("commit").get("author").get("name")))
