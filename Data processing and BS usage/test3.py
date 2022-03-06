

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


    # print(soup.get_text())
    # print(soup.select("div > #j-anime-nav-collect")[0].get_text())
    #查找所有div下id='j-anime-nav-collect'的标签内容，放在一个list里
    # print(soup.select("div > #j-anime-nav-collect"))



    # print(soup.select("ul > .item")[1].get_text())


    # print(soup.title.get_text())

    # print(soup.title.string)


    # print(soup.img)

    # print((soup.find_all('img')))


    # print(soup.find(class_='u-tt').get_text())


    list = soup.find('div',class_='lst-item').find_all('a',class_='u-card')

    for item in list:

        #取出所有list中的每一项的细节
        mingzi = item.find('p',class_='u-tt').get_text()

        print(mingzi)

        #取出图片地址
        pic_url = item.find('img').get("data-src")

        print(mingzi+'-------'+pic_url)


        # fenshu = item.find('span',class_='u-score').get_text()
        # print(fenshu)


        # print("___________________")
        # print(item)
        # print(list)




    pass





if __name__ == '__main__':
        main()
