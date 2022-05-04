# Requests
import requests
import pprint
import textwrap
import json
from requests_toolbelt.utils import dump

def connect_site(site):
    req = requests.get(site)
    print(type(req.status_code))
    if int(req.status_code) == 200:
        return req # req.content
    else:
        return 'Error: ' + str(req.status_code)

def dict_routines(name):
    # Use a breakpoint in the code line below to debug your script.

    r = connect_site('https://www.google.com')
    #if r.json().get('status') == 'OK':
    for item in r.json().get('data'):
            print(item.items())

    pprint.pprint(data) # .decode('utf-8'))
    print(f'{name}')  # Press ⌘F8 to toggle the breakpoint.

def print_roundtrip(response, *args, **kwargs):
    format_headers = lambda d: '\n'.join(f'{k}: {v}' for k, v in d.items())
    print(textwrap.dedent('''
        ---------------- request ----------------
        req.method: {req.method} req.URL: {req.url}
        req hdrs: {reqhdrs}

        req body: {req.body}
        ---------------- response ----------------
        res.status_code: {res.status_code} res.reason: {res.reason} res.url: {res.url}
        res hdrs: {reshdrs}

        res.text: {res.text}
    ''').format(
        req=response.request,
        res=response,
        reqhdrs=format_headers(response.request.headers),
        reshdrs=format_headers(response.headers),
    ))

if __name__ == '__main__':
    api_serv = 'httpbin.org'
    api_serv = 'www.microsoft.com/en-us'

    requests.get(f'https://{api_serv}/', allow_redirects=False, hooks={'response': print_roundtrip})
