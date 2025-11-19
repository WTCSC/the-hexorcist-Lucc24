d='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def q(n,o):
    t=0
    for p,c in enumerate(n[::-1]):
        t += d.index(c)*(o**p)
    return t
def f(n,o):
    if n==0:
        return'0'
    r=''
    while n>0:
        r=d[n%o]+r
        n//=o
    return r
a=input("Welcome to whatever this is maybe its a calculator idk \n Please enter the number you would like to convert: ")
s=int(input("Please enter the numbers current base (2-36): "))
t=int(input("Please enter the numbers target base (2-36): "))
z=f(q(a, s), t)
print(f"The number \"{a}\" is \"{z}\" in base-{t}.")


