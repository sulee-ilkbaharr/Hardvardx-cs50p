class Cat:
    #değişmesini istemediğimiz değişken için büyük harf
    MEOWS=3
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")
            
            
cat =Cat()
cat.meow()