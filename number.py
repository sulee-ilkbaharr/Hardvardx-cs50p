try:
    number = int(input("what is number?")) #cat 
except ValueError:
    print("x is not integer.")

else:
    #yukarıdaki kod başarılı olursa çalışır.(try).Eğer else ifaddesi olmazsa hata olmuş olsa bile bu kod çalışır ama biz else ile bunu önlüyoruz!
    print(f"x is {number}")
    
    
    
print(f"""
      ************************************************************************
      """)
 
 

def main2():
    x= get_int()
    print(f"x is {x}")
    

def get_int():
    while True:
        try:
            return int(input("What is x?"))
        except ValueError:
            pass



def main3():
    x= get_int("What is x?")
    print(f"x is {x}")
    

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main3()