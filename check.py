import requests
import hashlib
import sys

def request_api_data(query_char):
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check API & try again')
    return res

def get_pass_leak_count(hashes, my_hash):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == my_hash:
            return count
    return 0

def pwned_api_check(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1pass[0:5], sha1pass[5:]
    response = request_api_data(first5_char)
    print(response)
    return get_pass_leak_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was hacked {count} times... consider updating your password.')
        else:
            print(f'{password} has not been hacked.')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))