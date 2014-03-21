import urllib.request
import urllib.parse
import urllib.response
import http.cookiejar 
import http.client

def Login():
	x = True
	while x:
		ID = input("Please input student ID: ")
		PWD = input("Please input Password: ")
		data = {"ID": ID, "PWD": PWD, "Submit": "登入系統"}
		data = urllib.parse.urlencode(data)
		data = data.encode('big5')
		req = urllib.request.Request(url_login, data, header, None, None, 'POST')
		u = urllib.request.urlopen(req)
		web_string = u.read()
		web_string = web_string.decode('utf8')
		print(web_string)
		if ('登入錯誤' in web_string):
			print('登入錯誤')
			x = True
		else:
			print('登入成功!!!!')
			x = False

url_login = 'http://stucis.ttu.edu.tw/mobile/mobilelogin.php'
url_listed = 'http://stucis.ttu.edu.tw/selcourse/ListSelected.php'
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1897.3 Safari/537.36"}
cookie = http.cookiejar.CookieJar()

opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie))
urllib.request.install_opener(opener)
Login()

req = urllib.request.Request(url_listed, None, header, None, None, 'GET')
u = urllib.request.urlopen(req)



