from tkinter import *
import os
import requests
from bs4 import BeautifulSoup
def search():

    url="https://www.wikipedia.org"
    try:
        page=requests.get(url)
        if page.status_code==200:
            print('success')
        else:
            print('error',page.status_code)
            print('please check url address')
    except Exception as e:
        print(e)
        print('net not working or add wrong')

    soup = BeautifulSoup(page.text,'lxml')
    x=input("enter to search >> ")
    ff=x.replace(" ","_")
    v="https://en.wikipedia.org/wiki/"
    pp=v+ff
    print(pp)
    try:
        page1=requests.get(pp)
        if page1.status_code==200:
            print('success')
        else:
            print('error',page1.status_code)
            print('please check url address')
    except Exception as e:
        print(e)
        print('net not working or add wrong')
    soup1= BeautifulSoup(page1.text,'lxml')
    cc=soup1.find('p',class_="")
    # first_var.set("")
    data = cc.text
    print(data)
while True:
    search()
