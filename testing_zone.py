from urllib import parse

url = '/client-id=123123123&code=00000000'
print(parse.urlsplit(url).query)

