def area_rectangle(s1, s2):
    print(s1*s2)

def area_triangle(a, h):
    print(0.5*a*h)

def area_circle(r):
    print(3.14*r**2)

choice = int(input("The area of ​​which figure you want to calculate? \n 1) Rectangle; \n 2) Triangle; \n 3) Circle. \n Enter here number of Yuor choice: "))

if choice == 1:
    a = int(input('Enter side "a": '))
    b = int(input('Enter side "b": '))
    area_rectangle(a,b)
elif choice == 2:
    a = int(input('Enter side "a": '))
    h = int(input('Enter heigh of triangle "h": '))
    area_triangle(a, h)
elif choice == 3:
    r = int(input('Enter radius of cicle "r": '))
    area_circle(r)
else: 
    print("You have entered an incorrect number")