import http.client,re,json,random

class WoniuSalees:
    def __init__(self):
        self.host='localhost'
        self.port=8080
        self.cookie=''

    def test_login(self):
        conn=http.client.HTTPConnection(host=self.host,port=self.port)
        param='username=admin&password=admin123&verifycode=0000'
        header={'Content-Type':'application/x-www-form-urlencoded'}
        conn.request(method="POST",url='/user/login',body=param,headers=header)
        resp=conn.getresponse()
        cookie_list=resp.getheaders()
        for mycookie in cookie_list:
            if mycookie[0]=="Set-Cookie":
                self.cookie+=mycookie[1].split(";")[0]+";"
        print(self.cookie)

    def test_add_customer(self):
        sequence=random.randint(10000,99999)
        conn=http.client.HTTPConnection(host=self.host,port=self.port)
        param="customername=测试大侠&customerphone=18800%s&chlidsex=男&childdate=2013-07-01&creditkids=500&creditcloth=600"%sequence
        header={'Content-Type':'application/x-www-form-urlencoded','Cookie':self.cookie}
        conn.request(method="POST",url='/customer/add',body=param.encode('GBK'),headers=header)
        resp=conn.getresponse().read().decode()
        print(resp)
        if "add-successful"==resp:
            print('成功')
        else:
            print('失败')

if __name__ == '__main__':
    w=WoniuSalees()
    w.test_login()
    w.test_add_customer()