import requests
import hashlib
import sys

# password123 -> CBFDAC6008F9CAB4083784CBD1874F76618D2A97


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the api and try again')

    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':')
              for line in hashes.text.splitlines())  # generator object

    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)

  # same as above


def main(password_list):
    for password in password_list:
        count = pwned_api_check(password)
        if count:
            print(
                f'{password} was found {count} times... you should probably change your password')
        else:
            print(f'{password} was NOT found.  Carry on!')
    return 'done'


main(sys.argv[1:])
