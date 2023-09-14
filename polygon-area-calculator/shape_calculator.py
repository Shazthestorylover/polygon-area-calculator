'''
    Author: Shazzam Austin
    Course: Scientific Computing with Python
    Project: Budget App
    Website: FreeCodeCamp.org
    
    Date (Start): April 12, 2023
    Date (End): April 14, 2023
'''

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    '''Used to represent an instance of a Rectangle as a string.'''
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
        
    '''Sets the width of the polygon.'''
    def set_width(self, poly_width):
        self.width = poly_width

    '''Sets the height of the polygon.'''
    def set_height(self, poly_height):
        self.height = poly_height

    '''Returns area (width * height)'''
    def get_area(self):
        area = self.width * self.height
        return area
        
    ''' Returns perimeter (2 * width + 2 * height)'''
    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter

    '''Returns diagonal ((width ** 2 + height ** 2) ** .5)'''
    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** 0.5)
        return diagonal

    '''
        Returns a string that represents the shape using lines of "*".
        
        The number of lines should be equal to the height and the number of "*" 
        in each line should be equal to the width.

        There should be a new line (\n) at the end of each line. 
        If the width or height is larger than 50, this should 
        return the string: "Too big for picture.".
    '''
    def get_picture(self):
        char = '*'

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ((char*self.width) + "\n") * self.height
        return picture
            

    '''
        Takes another shape (square or rectangle) as an argument.

        Returns the number of times the passed in shape could fit 
        inside the shape (with no rotations).

        For instance, a rectangle with a width of 4 and a height 
        of 8 could fit in two squares with sides of 4.
    '''
    def get_amount_inside(self, shape_object):
        # Dividing the object's area by the 2nd shape object's area
        amount_of_times_shape_fits = (self.width // shape_object.width) * (self.height // shape_object.height)
        return amount_of_times_shape_fits




class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side

    '''Used to represent an instance of a square as a string.'''
    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side
