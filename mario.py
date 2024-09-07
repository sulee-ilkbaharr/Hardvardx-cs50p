def main():
    print_square3(3)
    
def print_square(size):
    for _ in range(size):
        print("#" *size, end="")
   
        
def print_square2(size):
    #for eachg row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        #otomatik satır sonu elde edersin
        print()
        
def print_square3(size):
    for _ in range(size):
        row(size)
        
        
def row(size):
        print("#" *size)       

main()
