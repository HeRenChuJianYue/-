


import requests
import json



def main():

    url = "https://json.tewx.cn/user/API_kdd531mytfdzm06i?sdAS1dsnuUa3sd=190001&Jsdh4bajs99dii=sohpuisypf4nfaei"

    resp = requests.get(url=url)
    # print(resp.content.decode("utf-8"))




    content = resp = resp.content.decode("utf-8")

    # print(type(content))

    print(content)
    #把字符串变成了字典
    shuju = json.loads(content)

    # print(shuju["code"])
    # 访问json转化后的字典
    print(shuju["data"]["JSON"]["mydata"]["name"])



    pass



if __name__ == '__main__':
    main()