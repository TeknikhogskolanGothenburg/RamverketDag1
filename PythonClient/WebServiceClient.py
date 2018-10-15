from urllib.parse import urlencode

import httplib2 as httplib2


def main():
    name = input("Please enter your name: ")
    h = httplib2.Http()
    _, content = h.request('http://localhost:51229/HelloWebService.asmx/GetMessage',
              'POST',
              urlencode({'name': f'{name}'}),
              headers={'Content-Type': 'application/x-www-form-urlencoded'}
              )

    _, content = content.decode('utf-8').split('\n')
    print(content[36:-9])

if __name__ == '__main__':
    main()
