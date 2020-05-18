# Importing math library
import math

#func1 to convert cartesian coordinate to polar
def get_polar():
    # Reading cartesian coordinate
    x = float(input('Enter value of x: '))
    y = float(input('Enter value of y: '))
    # Converting cartesian to polar coordinate
    # Calculating radius
    radius = math.sqrt( x * x + y * y )
    # Calculating angle (theta) in radian
    theta = math.atan(y/x)
    # Converting theta from radian to degree
    theta = 180 * theta/math.pi
    # if point in second or third quadrant make correction in theta
    if (x <= 0 and y >= 0) or (x < 0 and y < 0) :
        theta = 180 + theta
    # Displaying polar coordinates
    print('Polar coordinate is: (radius = %0.2f,theta = %0.2f)' %(radius, theta))

#func1 to convert polar coordinated to cartesian
def get_cart():
    # Reading polar coordinate
    r = float(input('Enter value of radius: '))
    theta = float(input('Enter value of theta in degrees: '))
    # Converting polar to cartesian coordinate
    # Converting theta from degreeto radian
    theta = math.pi * theta/180
    # calculating x-coordinate
    x = r * math.sin(theta)
    # calculating y-coordinate
    y = r * math.cos(theta)
    # Diplaying catesian coordinates
    print('Cartesian coordinate is: (x = %0.2f, y = %0.2f)' %(x, y))

# ask user to select conversion
a = int(input('enter 1 to convert cartesian to polar and 2 for vise-versa: '))
if a == 1:
    get_polar()
elif a == 2:
    get_cart()
else:
    print("Invalid input")
