# Chapter_8_Supp2
# Date: Feburary 19, 2015
# Created by: Zach Golik y Brianna Melius

class Prism(object):
    def __init__(self, ID, length = 0, width = 0, area = 0, perimeter = 0, height = 0, volume = 0):
        self.__ID = ID
        self.__length = length
        self.__width = width
        self.__area = area
        self.__perimeter = perimeter
        self.__height = height
        self.__volume = volume

    def __str__(self):
        print("ID:", self.__ID)
        print("Length:", self.__length)
        print("Width:", self.__width)
        print("Height:", self.__height)
        print("Perimeter:", self.__perimeter)
        print("Area:", self.__area)
        print("Volume:", self.__volume)

    def len_wid_hig_get(self):
        numLen = int(input("Please enter a number for length (over 1): "))
        while numLen < 2:
            numLen = int(input("Enter a number above 1: "))
        self.__length = numLen
        numWid = int(input("Please enter a number for width (over 1): "))
        while numWid < 2:
            numWid = int(input("Enter a number above 1: "))
        self.__width = numWid
        numHig = int(input("Please enter a number for height (over 1): "))
        while numHig < 2:
            numHig = int(input("Enter a number above 1: "))
        self.__height = numHig
        

    def per_area_vol(self):
        self.__perimeter = (self.__width * 2) + (self.__length * 2)
        self.__area = (self.__width * self.__length)
        self.__volume = (self.__length * self.__width * self.__height)
        

def main():
    prism1 = Prism(ID = "1")
    prism2 = Prism(ID = "2")
    prism3 = Prism(ID = "3")

    choice = None
    while choice != "0":
        print \
          ("""
          Prism Measures
          0 - Quit
          1 - Add prism measurments
          2 - Print rectangles
          """)
        
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # add rectangle measurements
        elif choice == "1":
            print("Prism 1")
            prism1.len_wid_hig_get()
            prism1.per_area_vol()
            print("\nPrism 2")
            prism2.len_wid_hig_get()
            prism2.per_area_vol()
            print("\nPrism 3")
            prism3.len_wid_hig_get()
            prism3.per_area_vol()

        # print rectangle
        elif choice == "2":
            prism1.__str__()
            print()
            prism2.__str__()
            print()
            prism3.__str__()

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")

