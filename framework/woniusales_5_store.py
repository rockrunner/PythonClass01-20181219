#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import requests
from PythonClass01.framework.data.support import Support
class Store_in:
     def __init__(self):
         self.support = Support()

     def queryinfo(self):
        data={'batchname':'GB20181221','goodsserial':'M1T1866D'}
        session=requests.session()
        resp=session.post('http://192.168.126.1:8080/store/queryinfo',data=data)
        print(resp.text)
     #
     def add(self):
        query_goods=self.support.query_one('select goodsserial from goods order by RAND() limit 0,1')
        print(query_goods)
     #    data={'batchname':'GB20181221','goodsserial':'M6S0637D','barcode':'6955203674869','inputsize':'66-73-80-90','goodstype':'衣服','quantity':'1'}
     #    session=requests.session()
     #    resp=session.post('http://192.168.126.1:8080/store/add',data=data)
     #    print(resp.text)

if __name__=='__main__':
    s=Store_in()
    # s.queryinfo()
    s.add()