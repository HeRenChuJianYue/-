

import requests
import json
from bs4 import BeautifulSoup


def main():
    url = "https://www.4399dmw.com/donghua/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Referer": "http://www.baidu.com"
    }

    resp = requests.get(url=url, headers=headers)

    # print(resp.content.decode("utf-8"))
    # 保存页面源代码
    html_doc = resp.content.decode("utf-8")

    # 使用bs去处理网页源代码

    soup = BeautifulSoup(html_doc)

    # 找到class_='m-hd'的div标签
    # print(soup.find("div",class_="m-hd"))
    # print(soup.find("ul",class_='u-tab'))
    # print(soup.find_all('a',class_='u-card')[3].get_text().strip())

    # 获取页面中有多少这种元素
    number = len(soup.find_all('a',class_='u-card'))
    # print(number)
    for i in range(number):
        # 获取某个元素的文字内容
        print(soup.find_all('a', class_='u-card')[i].get_text().strip())

    pass




if __name__ == '__main__':
    main()