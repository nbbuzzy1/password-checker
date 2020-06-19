import requests

# password123 -> CBFDAC6008F9CAB4083784CBD1874F76618D2A97

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
res = requests.get(url)
print(res)
