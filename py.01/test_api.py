from urllib.request import urlopen
request = urlopen('https://private-anon-be426ea5fb-poddapi.apiary-mock.com/funf').read()
print(request)