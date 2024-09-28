#NOTE:Tuple not mutuable(değiştirilemez!!!!

def main():
    student =get_student
    print(f"{student[0]} from {student[1]}")
    
#tuple , tuple immutable olduğu için artık indeksleyebilirim.
def get_student():
    n = input("Name: ")
    h = input("House: ")
    return (n,h) 

#böylece bir kütüphane oluşturduğum zaman sadece bu sayfayı terminalde çalıştırdığımda gerçekten main() fonksiyonunu getirir
if __name__ == "__main__":
    main()
    
    
    
    