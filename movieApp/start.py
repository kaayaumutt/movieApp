import movieApp

if __name__ == '__main__':
    print("Bu Uygulamadaki Bilgiler (https://www.fullhdfilmizlesene.pw/)'den alınmıştır.")
    vote = input("1-Yeni Filmler\n2-En Çok Beğenilen Filmler\n3-En Çok İzlenenler\nSeçim: ")
    #movieApp.Movie(vote)
    #Inheritiance,Crushing...
    name = input("İsminizi Giriniz: ")
    movieApp.MovieChild(vote,name)