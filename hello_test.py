from helloo import Hello

def test_default():
    assert Hello()== "Hello, World"
    
def test_argument():
 for name in ["Hermonie","Herry","Ron"]:
     assert Hello(name)==f"Hello, {name}"