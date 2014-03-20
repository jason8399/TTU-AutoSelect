import urllib.request
import urllib.parse
import urllib.response
import http.cookiejar 

ID = input("Please input student ID: ")
PWD = input("Please input Password: ")

url = "http://stucis.ttu.edu.tw/login.php"
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1897.3 Safari/537.36"}
data = {"ID": ID, "PWD": PWD, "Submit": "登入系統"}
data = urllib.parse.urlencode(data)
data = data.encode('big5')

req = urllib.request.Request(url, data, header,None,None,'POST')	#POST訊息
f = urllib.request.urlopen(req) 
cookie = f.getheader('Set-Cookie')	#get cookie
print ("the cookies are: ")
print(cookie)

header.update({'Cookie' : cookie})	#重組cookie
print(header)

ListSelected = "http://stucis.ttu.edu.tw/ListSelected.php"		#已選課程

req = urllib.request.Request(url,None,header,None,None,'GET')	#GET資料
f = urllib.request.urlopen(req)

#尚未完成 處理資訊
f = urllib.parse.unquote_to_bytes(f.read())
print(f)
