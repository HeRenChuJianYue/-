
import requests

def main():

    url = "http://sqlilabs.njhack.xyz/Less-20/"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        # "cookie":"uname=admin"
    }

    data={"uname":"admin","passwd":"admin"}

    # cookie_dict = {"uname":"admin"}
    # resp = requests.get(url,headers=headers,cookies=cookie_dict)
    resp = requests.post(url,headers=headers,data=data,verify=False,timeout=3)
    print(resp.content.decode("utf-8"))

    # #解码cookie
    # cookies = requests.utils.dict_from_cookiejar(resp.cookies)
    # print(cookies)
    # print(resp.content.decode("utf-8"))


    pass








if __name__ == '__main__':
    main()