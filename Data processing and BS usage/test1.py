
import requests
import json
from pprint import  pprint

def main():
    url = "http://127.0.0.1/test1.json"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Referer":"http://www.baidu.com"
    }


    resp = requests.get(url=url,headers=headers)

    json_str = resp.content.decode("utf-8")
    # print(json_str)

    ret1 = json.loads(json_str)
    # print(ret1["objects"][4]["EmailAddress"])
    # print(ret1)


    # 保存一下

    # with open("a.txt","w",encoding="utf-8") as f:
    #     # ensure_ascii-False 可以显示中文，indent=2 把子节点向后移动两个空格
    #     f.write(json.dumps(ret1,ensure_ascii=False,indent=2))
    # 美化打印
    # pprint(ret1)

    # 读取本地json文件
    with open("a.txt","r",encoding="utf-8") as f:
        ret2 = json.load(f)
        print(ret2["objects"])

    pass



if __name__ == '__main__':
    main()