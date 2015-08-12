# -*- coding: utf-8 -*-
import threading
import requests
import requests.models
import getpass
import time
from multiprocessing import Process, Pool


class AutoSelect:

    def __init__(self):
        self.urlLogin = "http://stucis.ttu.edu.tw/login.php"
        self.urlListed = "http://stucis.ttu.edu.tw/selcourse/ListClassCourse.php"
        self.urlSelect = "http://stucis.ttu.edu.tw/selcourse/DoAddDelSbj.php"
        self.urlSeltop = "http://stucis.ttu.edu.tw/menu/seltop.php"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1897.3 Safari/537.36"}
        self.response = ""
        self.cookies = ""
        self.courseList = ""
        self.__id = ""
        self.__pwd = ""
        pass

    def login(self):
        self.__id = input("Please input student ID: ")
        self.__pwd = getpass.getpass("Please input Password: ")
        data = {"ID": self.__id, "PWD": self.__pwd, "Submit": "登入系統"}
        self.response = requests.post(self.urlLogin, data=data, headers=self.headers)
        if "登入錯誤" in self.web_decode():
            print("Login failed")
            self.login()
        else:
            print("Login success!!!!")
            self.cookies = self.response.cookies

    def web_decode(self):
        web_string = self.response.text
        web_string = web_string.encode(self.response.encoding)
        return web_string.decode("big5")

    def open_file(self):
        print("Please Check 'list.txt' is under same folder")
        input("Please press any key to continue......")
        try:
            file = open("list.txt")
        except FileNotFoundError:
            print("File Not Found!!")
            exit(0)
        self.courseList = file.readlines()
        for x in range(0, len(self.courseList)):
            self.courseList[x] = self.courseList[x].strip("\n")

    def do_select(self):
        self.response = requests.get(self.urlSeltop, headers=self.headers, cookies=self.cookies)
        self.response = requests.get(self.urlListed, headers=self.headers, cookies=self.cookies)
        for y in range(2):
            for courseId in self.courseList:
                params = {"AddSbjNo": courseId}
                test = self.Select(self, params)
                test.start()

    class Select(threading.Thread):
        def __init__(self, outter, params):
            threading.Thread.__init__(self)
            self.params = params
            self.outter = outter

        def run(self):
            while True:
                try:
                    self.response = requests.get(self.outter.urlSelect, params=self.params, headers=self.outter.headers,
                                                 cookies=self.outter.cookies, timeout=3)
                    print(self.response.status_code)
                except requests.exceptions.Timeout:
                    print("TIMEOUT" + str(self.params))
                    pass

    def check_time(self):
        #unavailable
        pass


if __name__ == "__main__":
    auto = AutoSelect()
    auto.login()
    auto.open_file()
    auto.do_select()
