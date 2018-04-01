import time
import requests
from bs4 import BeautifulSoup
import re
import tkinter
from lxml import etree
import codecs

class Net(object):
    def __init__(self):
        # self.gi = pygeoip.GeoIP("./GeoLiteCity.dat")
        self.root = tkinter.Tk()
        self.root.title("sousuo zcw")
        # 窗口标题
        self.ip_input = tkinter.Entry(self.root, width=80)
        # 窗口尺寸
        self.display_info = tkinter.Listbox(self.root, width=150)
        # 创建一个回显列表
        self.result_button = tkinter.Button(self.root, command = self.run,text="!!!!!!!gogogog!!!!!!!")
        # 查询结果的按钮

    def gui_arrang(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()

    def run(self):
        url = requests.get("http://www.sosobt.net/s/%s"%(self.ip_input.get())).content
        soup = BeautifulSoup(url, "lxml")
        first = soup.select_one('.r').select_one('a')
        first_href = "http://www.sosobt.net/%s"%(first.get('href'))
        get_detail = requests.get(first_href).content
        get_detail = BeautifulSoup(get_detail, "lxml")
        thunder = get_detail.select_one('a[href*="thunder://"]')
        self.display_info.insert(0, thunder.get('href'))

def main():
    # 初始化对象
    FL = Net()
    # 进行布局
    FL.gui_arrang()
    # 主程序执行
    tkinter.mainloop()
    pass


if __name__ == "__main__":
    main()








