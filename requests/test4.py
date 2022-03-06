
import requests

def main():

    url = "http://sqlilabs.njhack.xyz/Less-20/index.php"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    data = {"uname":"admin","passwd":"admin"}

    #实列化session
    session = requests.session()


    #发送post请求，提交用户名和密码
    session.post(url,headers=headers,data=data)
    #此时session里面已经有cookie的信息的，可以直接用session去get登录后的任何页面
    res = session.get(url,headers=headers)
    print(res.content.decode("utf-8"))



    pass








if __name__ == '__main__':
    main()