import urllib.request
import urllib.parse
import urllib.response
import http.cookiejar 
import http.client
########################################副程式區######################################################
def showMenu():
	print("Welcome To Use ASCS for TTU")
	print("Please Selected The function")
	print("1.Read Selected Course")


def webDecodeBig5(web_string):			#web資料Decode BIG5
	web_string = web_string.read()
	return web_string.decode('big5')

def Login():
	x = True
	while x:
		ID = input("Please input student ID: ")
		PWD = input("Please input Password: ")
		data = {"ID": ID, "PWD": PWD, "Submit": "登入系統"}
		data = urllib.parse.urlencode(data)
		data = data.encode('big5')
		req = urllib.request.Request(url_login, data, header, None, None, 'POST')
		if ('登入錯誤' in webDecodeBig5(urllib.request.urlopen(req))):
			print('登入錯誤')
			x = True
		else:
			print('登入成功!!!!')
			x = False

def readSelectedList():	#Select Course List
	req = urllib.request.Request(url_listed, None, header, None, None, 'GET')
	u = urllib.request.urlopen(req)
	web_string = webDecodeBig5(urllib.request.urlopen(req))
	if ('Not login or session expire!' in web_string):
		print("You need to Login again........\n")
		Login()
		readSelectedList()
	else:
		print(web_string)
#########################################物件區######################################################
url_login = 'http://stucis.ttu.edu.tw/login.php'
url_listed = 'http://stucis.ttu.edu.tw/selcourse/ListSelected.php'
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1897.3 Safari/537.36"}
cookie = http.cookiejar.CookieJar()
flag = True
########################################主程式區######################################################
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie)) #cookie處理
urllib.request.install_opener(opener)

Login()
showMenu()
select = input('select = ')
readSelectedList()





