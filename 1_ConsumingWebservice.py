# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 17:29:50 2021

@author: Lakshmi
"""

import requests

base_url ="https://peter-htet.outsystemscloud.com/ITDInterviews/rest/Users/"

def get_all_users():
    x = requests.get(base_url+'GetAllUsers')
    print(x.text,x.status_code, x.reason)

def get_a_user(name):
    x = requests.get(base_url+'GetUser?name='+name)
    print(x.text,x.status_code, x.reason)

def delete_a_user(uid):
    if type(uid)!= str:
        uid = str(uid)
    x = requests.get(base_url+'DeleteUser?id='+uid) 
    print(x.text,x.status_code, x.reason)

def post_a_user(data):
    x = requests.post(base_url+"AddUpdateUser", json=data)
    print(x.text,x.status_code, x.reason)

data = {"Id": 0, "name": "Abc Xyz", "email": "abc_xyz@gmail.com", "password": "sqwertyuiop","phone": "12345678"}