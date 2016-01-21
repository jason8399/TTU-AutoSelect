# -*- coding: utf-8 -*-
import threading
import requests
import time
import configparser


class AutoSelect:

    def __init__(self):
        self.urlLogin = "https://stucis.ttu.edu.tw/login.php"
        self.urlListed = "https://stucis.ttu.edu.tw/selcourse/ListClassCourse.php"
        self.urlSelect = "https://stucis.ttu.edu.tw/selcourse/DoAddDelSbj.php"
        self.urlSeltop = "https://stucis.ttu.edu.tw/menu/seltop.php"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1897.3 Safari/537.36"}
        self.response = ""
        self.cookies = ""
        self.config = configparser.ConfigParser()
        self.config.read("config.conf")
        self.courseList = eval(self.config["DEFAULT"]["CourseList"])
        self.__id = self.config["DEFAULT"]["Account"]
        self.__pwd = self.config["DEFAULT"]["Password"]
        self.time = self.config["DEFAULT"]["Time"]
        self.thread_num = int(self.config["DEFAULT"]["Thread"])
        pass

    def login(self):
        data = {"ID": self.__id, "PWD": self.__pwd, "Submit": "登入系統"}
        web_decode = lambda self : self.response.text.encode(self.response.encoding).decode("big5")
        while True:
            try:
                self.response = requests.post(self.urlLogin, data=data, headers=self.headers, timeout=3)
                if "登入錯誤" in web_decode(self):
                    print("Login failed")
                else:
                    print("Login success!!!!")
                    self.cookies = self.response.cookies
                    break
            except requests.exceptions.Timeout:
                print("LOGIN_TIMEOUT!")

    def do_select(self):
        self.response = requests.get(self.urlSeltop, headers=self.headers, cookies=self.cookies)
        self.response = requests.get(self.urlListed, headers=self.headers, cookies=self.cookies)
        for y in range(self.thread_num):
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
        self.time = time.mktime(time.strptime(self.time, '%Y/%m/%d %H:%M:%S'))
        print("Waiting...")
        while True:
            now_time = time.mktime(time.localtime())
            if now_time >= self.time:
                break
        print("Start!")
        pass


if __name__ == "__main__":
    auto = AutoSelect()
    auto.check_time()
    auto.login()
    auto.do_select()
