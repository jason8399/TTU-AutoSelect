import urllib.request
import urllib.parse
import urllib.response
import http.cookiejar 
import http.client
import os
########################################副程式區######################################################
def showMenu():
	print("Welcome To Use ASCS for TTU")
	print("Please Selected The function")
	print("1.Read Selected Course")
	print("2.Read Score")
	print("5.Exit")

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
		input('任意鍵繼續......')

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

def readScore():
	req = urllib.request.Request(url_Score, None, header, None, None, 'GET')
	u = urllib.request.urlopen(req)
	web_string = webDecodeBig5(urllib.request.urlopen(req))
	if ('Not login or session expire!' in web_string):
		print("You need to Login again........\n")
		Login()
		readScore()
	else:
		print(web_string)
#########################################物件區######################################################
url_login = 'http://stucis.ttu.edu.tw/login.php'
url_listed = 'http://stucis.ttu.edu.tw/selcourse/ListSelected.php'
url_Score = 'http://stucis.ttu.edu.tw/academic/listscore.php'
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1897.3 Safari/537.36"}
cookie = http.cookiejar.CookieJar()
flag = True
########################################主程式區######################################################
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie)) #cookie處理
urllib.request.install_opener(opener)

os.system('clear')
Login()
while True:
	os.system('clear')
	showMenu()
	select = input('select = ')
	if select == '1':
		readSelectedList()
	elif select == '2':
		readScore()
	elif select == '5':
		print('\n\nGood Bye!!!!')
		os._exit(0)
	input('任意鍵繼續......') 






