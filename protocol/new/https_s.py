#!/usr/bin/env python
# -*- coding:utf-8 -*-  
#====#====#====#====   
#Author:
#CreatDate:
#Version: 
#====#====#====#====
import requests
resp=requests.post('http://www.oschina.net',verify=False)
resp.encoding='utf-8'
print(resp.text)
