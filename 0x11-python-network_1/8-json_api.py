#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == '__main__':
    import requests
    import sys

    q = ''
    if len(sys.argv) > 1:
        q = sys.argv[1]

    try:
        result = requests.post(
            'http://0.0.0.0:5000/search_user', data={'q': q})
        result.json()
        if 'id' in result and 'name' in result:
            print('[{}] {}'.format(result['id'], result['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
