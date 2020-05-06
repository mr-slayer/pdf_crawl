from django.shortcuts import render
import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup
import sqlite3
import time
from selenium import webdriver
def temp(request):
    dlink=request.GET['link']
    
##    driver=webdriver.Chrome("C:/Users/HP/Downloads/chromedriver_win32/chromedriver")
##    #driver.get("https://www.pdfdrive.com/living-in-the-light-a-guide-to-personal-transformation-d10172273.html")
    driver=webdriver.Chrome('chromedriver.exe')
    driver.get(dlink)
    time.sleep(10)
    r=driver.page_source
    f_link=[]
    soup = BeautifulSoup(r, 'html.parser') 
    for link in soup.findAll('a', attrs = {'class':'btn btn-primary btn-user'}):
        if(link.get("href")!='[]'):
            f_link.append('https://www.pdfdrive.com'+link.get("href"))
    soup1 = BeautifulSoup(r, 'html.parser') 
    for link in soup1.findAll('a', attrs = {'class':'btn btn-success btn-responsive'}):
        if(link.get("href")!='[]'):
            f_link.append(link.get("href"))
    driver.close()
    print(f_link)
    return HttpResponse(f_link[0])


def search(request):
    conn = sqlite3.connect("pdf_drive.db")
    cur = conn.cursor()
    print(cur)
    query=request.GET['q']
    query="'%"+query+"%'"
    #params = (query)
    cur.execute("""SELECT name,image,page,size,link FROM ebook WHERE name LIKE"""+query+ """;""")
    # cur.execute("SELECT * FROM ebook WHERE name MATCH query;")

    rows = cur.fetchall()

    return render(request,"search.html",{'h':rows})
def home(request):
    conn = sqlite3.connect("pdf_drive.db")
    cur = conn.cursor()
    print(cur)
    cur.execute("SELECT name,image,page,size,link FROM ebook limit 100;")
    rows = cur.fetchall()
    return render(request, 'temp.html',{'h':rows})
