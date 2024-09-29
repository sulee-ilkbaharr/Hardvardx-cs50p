def main():
    yell(["This", "is" ,"CS50"])
    
#tek yıldız listeyi tanımlıyor, çift yıldız dict 'i
def yell(*words):
    # uppercase=[]
    # for word in words:
    #     uppercase.append(word.upper())
    # print(*uppercase)
    uppercased= [word.upper() for word in words]
        
        
if __name__=="__main__":
    main()