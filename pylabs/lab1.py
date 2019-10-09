import math
choice = input("Выберете функцию:1-G,2-F,3-Y " )

if choice =="1":
    a = float(input())
    x = float(input())
    q = (4*(-4*(a**2)+a*x+5*(x**2)))
    w = (-20*(a**2)+28*a*x+3*(x**2))
    G = q/w
    if ( w == 0) :
        print("Ошибка")
    else:
        print("G = %.2f "%G)
elif choice =="2" :
    a=float(input())
    x=float(input()) 
    F=(math.atan(24*(a**2)-25*a*x+6*(x**2)))
    print("F = %.2f"%F )
elif choice == "3":
    a=float(input())
    x=float(input())
    Y = math.log(2*(a**2)-7*a*x+6*(x**2)+1)
    print("Y = %.2f "% Y)
else:
    print("Ошибка ввода")
