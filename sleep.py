def main():
    n = int(input("What'n n?"))
    for s in sheep(n):
        print(s)
        
# def sheep(n):
#     flock=[]
#     for i in range(n):
#         flock.append("🐏"*i)
#     return flock

#çok fazla koyunu aynı anda istersem bunun için bir python generatörü olan yiled ' ı kullanmalıyım.Bu ürettiği kadarını bastırarakbellek sorunu yener . try n=100000.  her seferinde bir sıra koyun üretir.
def sheep(n):
    for i in range(n):
        yield "🐏" *i

if __name__=="__main__":
    main()