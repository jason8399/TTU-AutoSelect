import urllib.request
import urllib.parse
import urllib.response
import http.cookiejar 
import http.client

ID = input("Please input student ID: ")
PWD = input("Please input Password: ")

header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1897.3 Safari/537.36"}
data = {"ID": ID, "PWD": PWD, "Submit": "登入系統"}
data = urllib.parse.urlencode(data)
data = data.encode('big5')

#Login
try:
	h1 = http.client.HTTPConnection('stucis.ttu.edu.tw',80)
	h1.request('GET' , '/login.php', None, header)
	response = h1.getresponse()
	print (response.status)
	print (response.reason)
	print (response.read())
	print (response.getheaders())
	cookie = response.getheader('Set-Cookie')
	print (cookie)
except (Exception, e):
    print (e)
    h1.close()

#cookie split
cookie = cookie.split()
cookie = cookie[4].split(';')
cookie = cookie[0]
header.update({"Cookie" : cookie})
print(header)

try:
	h1.request('POST', '/login.php', data, header)
	response = h1.getresponse()
	print (response.status)
	print (response.reason)
	print (response.read())
	print (response.getheaders())
except (Exception, e):
    print (e)
    h1.close()

h1.close()

#h1.request('GET', '/selcourse/ListSelected.php', None, header)
#response = h1.getresponse()
#print (response.status)
#print (response.reason)
#print (response.read())
#print (response.getheaders())


h1.close()

