import requests
import json
from bs4 import BeautifulSoup


def pachong(page):
    url = "https://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/".format(page)
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

    list = soup.find('div', class_='lst').find_all('a', class_='u-card')

    for item in list:
        # 取出所有list中的每一项的细节
        # mingzi = item.find('p', class_='u-tt').get_text()
        mingzi = item.find('p', class_='u-tt').string

        # 取出图片地址
        pic_url = item.find('img').get("data-src")

        print(mingzi + '-------' + "http:" + pic_url)


    pass



def main():
    url = "https://www.4399dmw.com/huoying/donghua/"
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

    # print(soup.find_all('div',class_='works__info'))

    list = soup.find_all('div',class_='works__info')[3].find_all('a')

    # print(list)
    for item in list:
        print(item.get_text())
    pass

if __name__ == '__main__':
    main()