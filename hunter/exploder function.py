list = ["guvi"] 
def a(x):
     print x * 5
def main(fun, list):
     for item in list:
         fun(item)
main(a, list)

