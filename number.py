try:
    number = int(input("what is number?")) #cat 
except ValueError:
    print("x is not integer.")

else:
    #yukarıdaki kod başarılı olursa çalışır.(try).Eğer else ifaddesi olmazsa hata olmuş olsa bile bu kod çalışır ama biz else ile bunu önlüyoruz!
    print(f"x is {number}")