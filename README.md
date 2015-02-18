# Chapter_8_Supp
Supplementary exercises for Chapter 8

EXERCISE 1:

Create a class called rectangle.  The attributes for rectangle are:
    ID  - based off of a class attribute (page 222)
    Length - cannot be less than one
    Width - cannot be less than one
  
  The methods are:
    get and set methods for length and width (4 total)
    perimeter - returns the perimeter
    area - returns the area
    __init__ - creates the class, assigns the ID based on the current value of the ID class attribute, then increments the class                   ID, then calls the set methods to get length and width from the user.
    __str__ returns a string that prints the following:
                  Rectangle ID: #
                  Length: ##
                  Width: ##
                  Perimeter: ##
                  Area: ##
    
    your program should create 3 rectangles, and then print the results of each of them.
    
    EXERCISE 2
    Create a class called Prism, which does all the same things as rectangle, excpet that it uses a third attribute: Height.
    
    also, it should have sets and gets for height, and include a new method: volume, which returns the volume of the prism.
