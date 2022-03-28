def squarearea(x):
    return x*x


def rectperimeter(l, b):
    return 2*(l+b)


def rectarea(l, b):
    return l*b


if __name__ == "__main__":
    while True:
        print("Select an option from menu")
        print("1.Calculate Area of Square ")
        print("2.Calculate Perimeter of Rectangle  ")
        print("3.Calculate Area of Rectangle  ")
        print("4.Exit ")

        choice = int(input("Enter a choice: "))

        if choice == 1:
            a = int(input("Enter side of Square: "))
            area = squarearea(a)
            print("Area of Square is ", area)

        elif choice == 2:
            l = int(input("Enter Length of Rectangle: "))
            b = int(input("Enter Breadth of Rectangle: "))
            peri = rectperimeter(l, b)
            print("Perimeter of Rectangle is ", peri)

        elif choice == 3:
            l = int(input("Enter Length of Rectangle: "))
            b = int(input("Enter Breadth of Rectangle: "))
            area = rectarea(l, b)
            print("Area of Rectangle is ", area)

        elif choice == 4:
            break

        else:
            print("Invalid Option")


