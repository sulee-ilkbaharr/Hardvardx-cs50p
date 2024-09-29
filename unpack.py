# def total(galleons, sickles, knuts):
#     return (galleons*17+sickles)*29 +knuts

# # coins=[100,50,25]
# # print(total(*coins), "knuts")

# coins={"galleons":100, "sickles":50,"knuts":25}
# print(total(**coins), "knuts")


#kwargs behaviour like dictionary
def f(*args, **kwargs):
    print("Named:" ,kwargs)
    
f(galleons=100, sickles=50, knuts=25)