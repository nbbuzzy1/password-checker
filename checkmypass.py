import requests
import hashlib

# password123 -> CBFDAC6008F9CAB4083784CBD1874F76618D2A97


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')

    return res


def pwned_api_check(password):
    # check password if it exists in API response
    return hashlib.sha1(password.encode('utf-8')).hexdigest().upper()


pwned_api_check('password123')  # same as above
