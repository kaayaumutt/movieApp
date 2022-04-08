import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Movie:
    def __init__(self,option):
        self.url = "https://www.fullhdfilmizlesene.pw/"
        self.option = option
        self.control(option)
        self.dateTime = datetime.now()
        print(f"Güncel Tarih: {datetime.ctime(self.dateTime)}")

    def control(self,option):
        if option=="1":
            self.newMovie()
        elif option=="2":
            self.bestLike()
        elif option=="3":
            self.mostViewed()
        else:
            print("Hatalı Giriş Yaptınız.")
    
    def newMovie(self):
        html = requests.get(self.url+"yeni-filmler-izle").content
        self.dataReach(html)
    
    def bestLike(self):
        html = requests.get(self.url+"en-cok-begenilenler").content
        self.dataReach(html)

    def mostViewed(self):
        html = requests.get(self.url+"en-cok-izlenen-filmler").content
        self.dataReach(html)
    
    def dataReach(self,html):
        soup = BeautifulSoup(html,'html.parser')
        list = soup.find('div',{"class":"index-orta"}).find("ul").find_all("li",limit=15)
        count=1
        for i in list:
            name = i.find("div",{"class":"dty"}).find("h2").text
            category = i.find("div",{"class":"dty"}).find("span").text
            language = i.find("div",{"class":"dty"}).find("span").findNextSibling().text
            releaseDate = i.find("div",{"class":"dty"}).find("span").findNextSibling().findNextSibling().text.strip("Filmleri")
            imdbPuan = i.find("div",{"class":"dty"}).find("span").findNextSibling().findNextSibling().findNextSibling().text
            print(f"{count}.Filmin İsmi: {name}\n\tKategorisi: {category}\n\tDil Seçenekleri: {language}\n\tÇıkış Tarihi: {releaseDate}\n\tIMDB Puanı: {imdbPuan}")
            count+=1

class MovieChild(Movie):
    def __init__(self,option,name):
        super().__init__(option)
        self.name = name
        print(f"İşlemi Yapan Kişi {self.name} ve Class MovieChild")