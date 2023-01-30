#Using the Point class that is already there in the file, please do this:
# * Create an instance of the Point class with coordinates (0, 0) and put it in a variable named `first_instance`
# * Create an instance of the Point class with coordinates (0, 2) and put it in a variable named `second_instance`
# * Create an instance of the Point class with coordinates (2, 0) and put it in a variable named `third_instance`
# * On `first_instance`, write a call to the `move_right()` method.
# * Try running the program, and confirm that there are no errors that show up.

class Point:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
    
    def move_right(self):
        self.x += 1
        
    def move_left(self):
        self.x -= 1

    def move_up(self):
        self.y += 1
        
    def move_down(self):
        self.y -= 1

# please add your code here
first_instance=Point(0,0)
second_instance= Point(0,2)
third_inatance= Point(2,0)
first_instance.move_right()