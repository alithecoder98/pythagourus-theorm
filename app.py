import math
def pyt():
    a=int(input("enter side a length:"))
    b=int(input("enter side b length:"))
    c=math.sqrt((b**2)+(a**2))
    print(f"side c of the triangle is {c}units")
if __name__=="__main__":
    pyt()
    5