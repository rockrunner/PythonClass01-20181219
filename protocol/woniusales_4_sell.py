#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====

import requests,json
# from PythonClass01.framework.data.support import support
# data={'username':'admin','password':'admin123','verifycode':'0000'}
# resp=requests.post('http://localhost:8080/user/login',data=data)
# print(resp.text)
class Woniusales:
    def __init__(self):
        # self.support=support()
        pass
    def login(self):
         session=requests.session()
         data={"userName:WNCD000","userPass:woniu123","checkcode:0000"}
         resp=session.post('http://192.168.1.130:8080/WoniuBoss2.5/',data=data)
         # print(resp.text)
         if resp.text=='login-pass':
             print('首页登陆测试成功')
         else:
             print('首页登陆测试失败')

    def sell_barcode(self):

        data={'barcode':'6955203636348'}
        session=requests.session()
        resp=session.post('http://192.168.1.22:8080/sell/barcode',data=data)
        # print(resp.text)
        if '超人披风套装' in resp.text:
            print("'请扫描商品条码'测试成功")
        else:
            print("'请扫描商品条码'测试失败")


    # def phone(self):
    #     sql='select customerphone from customer oder by RAND() limit 1'
    #     customer_phone=self.support.query_one(sql)[0]
    #
    #
    #     data={'query':customer_phone}
    #     session=requests.session()
    #     resp=session.post('http://192.168.1.22:8080/customer/phone',data=data)
    #
    #     resp_dict=json.loads(resp.text)
    #     print(resp_dict)
    #     if resp_dict[0]['customerphone']==customer_phone:
    #         print(f'会员信息查询成功，手机号为{resp_dict[0][]customer_phone}')
    #     else:
    #         print(f'会员信息查询失败，输入的手机号为{customer_phone}')

    def phone_query(self):
        data={'customerphone':'13518212303'}
        session = requests.session()
        resp = session.post('http://192.168.1.22:8080/customer/query',data=data )
        print(resp.text)


    def summry(self,sellsumid):

        data={'sellsumid':'%s'%sellsumid,'barcode':'6955203636348','goodsserial':'M8Q9066C','goodsname':'超人披风内裤套装','goodssize':'80','unitprice':'139','discountratio':'68','discountprice':'94.52','buyquantity':'1','subtotal':'94.52'}
        session = requests.session()

        resp=session.post('http://192.168.1.22:8080/sell/detail',data=data)
        # print(resp.text)
        if resp.text=='pay-successful':
            print('确认收款测试成功')
        else:
            print("确认收款测试失败")



if __name__=='__main__':
    w=Woniusales()
    w.login()
    # w.sell_barcode()
    # w.phone()
    # w.phone_query()
    # w.summry()