import requests



def main():
    url="https://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/"
    url_list = []
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    for i in range(3):
        url_list.append(url.format(i))


     #打印地址列表
    print(url_list)


     #遍历地址列表并且发送get请求，然后保存
    for item in url_list:

        resp = requests.get(url=item,headers=headers)
        with open("a"+str(i)+".txt","wb+") as f:
            #写入文件
            f.write(resp.content)

    pass




if __name__ == '__main__':
    main()