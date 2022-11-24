import requests
import hashlib

def request_api_data(query_char):
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check API & try again')
    return res

def pwned_api_check(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pass[0:5], sha1pass[5:]
    response = request_api_data(first5_char)
    return response