# Chapter 8 Supp Exercises 1
# February 18, 2015
# By: Brianna Melius and Zach Golik

class Rectangle(object):
    def __init__(self, ID, length, width, area, perimeter):
        self.__ID = ID
        self.__length = length
        self.__width = width
        self.__area = area
        self.__perimeter = perimeter

    def __str__(self):
        print("ID:", self.__ID)
        print("Length:", self.__length)
        print("Width:", self.__width)
        print("Perimeter:", self.__perimeter)
        print("Area:", self.__area)

    def len_wid_get(self):
        numLen = int(input("Please enter a number for length (over 1): "))
        while numLen < 2:
            numLen = int(input("Enter a number above 1: "))
        self.__length = numLen
        numWid = int(input("Please enter a number for width (over 1): "))
        while numWid < 2:
            numWid = int(input("Enter a number above 1: "))
        self.__width = numWid

    def per_area(self):
        self.__perimeter = (self.__width * 2) + (self.__length * 2)
        self.__area = (self.__width * self.__length)

def main():
    rect1 = Rectangle(ID = "1", length = 0, width = 0, area = 0, perimeter = 0)
    rect2 = Rectangle(ID = "2", length = 0, width = 0, area = 0, perimeter = 0)
    rect3 = Rectangle(ID = "3", length = 0, width = 0, area = 0, perimeter = 0)

    choice = None
    while choice != "0":
        print \
          ("""
          Rectangle Measures
          0 - Quit
          1 - Add rectangle measurments
          2 - Print rectangles
          """)
        
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # add rectangle measurements
        elif choice == "1":
            print("Rectangle 1")
            rect1.len_wid_get()
            rect1.per_area()
            print("\nRectangle 2")
            rect2.len_wid_get()
            rect2.per_area()
            print("\nRectangle 3")
            rect3.len_wid_get()
            rect3.per_area()

        # print rectangle
        elif choice == "2":
            rect1.__str__()
            rect2.__str__()
            rect3.__str__()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
