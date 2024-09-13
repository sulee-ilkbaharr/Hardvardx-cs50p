from calculator import square
def main():
     test_negatif
     test_positif
     test_zero
    
# def test_square():
#     try:
#         assert square(2)==4
#     except AssertionError:
#         print("2 square was not 4!")
#     try:
#         assert square(3)==9
#     except AssertionError:
#         print("3 square was not 9")

def test_positif():
    assert square(2)==4
    assert square(3)==9
def test_negatif():
    assert square(-2)==4
    assert square(-3)==9
def test_zero():
    assert square(0)==0
    
        
        
if __name__ == "__main__":
    main()