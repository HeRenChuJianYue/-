import requests



def main():
    url="https://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/"

    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    #代理
    proxies = {"HTTP":"http://106.54.128.253:999"}
    urla = url.format("1")
    print(url)
    
    resp = requests.get(url=urla,headers=headers,proxies=proxies)
    with open("a.txt","wb+") as f:
        #写入文件
        f.write(resp.content)

    pass




if __name__ == '__main__':
    main()