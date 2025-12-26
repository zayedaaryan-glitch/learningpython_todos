
try:
    length = int(input("enter the length of the rectangle: "))
    width = int(input("enter the width of the rectangle: "))
    if length != width:
        area = length * width
        print(f'area of rectangle: {area}')
    else :
        exit("its a square")
except ValueError:
    exit("invalid input")





