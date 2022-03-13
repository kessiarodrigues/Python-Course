import urllib
import urllib.request


try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Erro')
else:
    print('ok')
    print(site.read())