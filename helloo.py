def main():
    name = input("what is your name?")
    print(Hello(name))
def Hello(to="World"):
    return f"Hello, {to}"

if __name__=="__main__":
    main()
    
    