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
        self.config = configparser.ConfigParser()
        self.config.read("config.conf")
        self.courseList = eval(self.config["DEFAULT"]["CourseList"])
        self.id = self.config["DEFAULT"]["Account"]
        self.pwd = self.config["DEFAULT"]["Password"]
        self.time = self.config["DEFAULT"]["Time"]
        self.thread_num = int(self.config["DEFAULT"]["Thread"])
        requests.packages.urllib3.disable_warnings()
        pass

    def do_select(self):
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
            self.response = ""
            self.cookies = ""
            self.headers = self.outter.headers.copy()
            self.thread_id = threading.get_ident()
            self.login()

        def login(self):
            data = {"ID": self.outter.id, "PWD": self.outter.pwd, "Submit": "登入系統"}
            web_decode = lambda self : self.response.text.encode(self.response.encoding).decode("big5")
            while True:
                try:
                    self.response = requests.post(self.outter.urlLogin, data=data, headers=self.headers, verify=False, timeout=3)
                    if "登入錯誤" in web_decode(self):
                        print("[Thread %d]Login failed" % self.thread_id)
                    else:
                        print("[Thread %d]Login success!!!!" % self.thread_id)
                        self.cookies = self.response.cookies
                        break
                except requests.exceptions.Timeout:
                    print("LOGIN_TIMEOUT!")

        def run(self):
            self.response = requests.get(self.outter.urlSeltop, headers=self.headers, cookies=self.cookies, verify=False)
            self.response = requests.get(self.outter.urlListed, headers=self.headers, cookies=self.cookies, verify=False)
            while True:
                try:
                    self.response = requests.get(self.outter.urlSelect, params=self.params, headers=self.headers,
                                                 cookies=self.cookies, verify=False, timeout=3)
                    print("[Thread %d]" % self.thread_id, self.response.status_code, self.params)
                    if "Not login or session expire!" in self.response.text:
                        self.login()
                    else:
                        time.sleep(1)
                except requests.exceptions.Timeout:
                    print("[Thread %d]TIMEOUT" % self.thread_id + str(self.params))
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
    auto.do_select()
