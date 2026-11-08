import ctypes

class ArrayList():

    def create_array(self, k):
        return (ctypes.py_object * k)()

    # Initializing list with predetermined capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.current = 0
        self.Array = self.create_array(self.capacity)

    # Move to start
    def move_to_start(self):
        self.current = 0
        print("Current pointer set to START of the list!")

    # Move to end
    def move_to_end(self):
        self.current = self.length
        print("Current pointer set to END of the list!")

    # Move to next
    def move_to_next(self):
        if (self.current < self.length):
            self.current += 1
            print("Current pointer set to NEXT element of the list!")
        else:
            print("Current pointer is at the end of the list!")

    # Move to previous
    def move_to_previous(self):
        if (self.current != 0):
            self.current -= 1
            print("Current pointer set to PREVIOUS element of the list!")
        else:
            print("Current pointer is at the start of the list!")

    # Move to custom position
    def move_to_position(self, position):
        if ((position < 0) or (position > self.length)):
            print("Given position is out of range!")
        else:
            self.current = position
            print("Current pointer set to position:" + str(position))

    # Adding element to the end of the list
    def add(self, x):
        if (self.length < self.capacity):
            self.Array[self.length] = x
            self.length += 1
            print("Element added successfully!")
        else:
            print("Capacity full!")

    # Left partition length
    def l_length(self):
        return self.current

    # Right partition length
    def r_length(self):
        return self.length - self.current

    # Inserting element at current position
    def insert(self, x):
        if (self.length < self.capacity):
            for i in range(self.length, self.current, -1):  # Elements from end of array to current pointer
                self.Array[i] = self.Array[i - 1]  # shifts one place to the right
            self.Array[self.current] = x
            self.length += 1
            print("Successfully inserted element " + str(x) + " at pointer position " + str(self.current))
        else:
            print("Capacity full!")

    # Removing/Deleting current element - element value to the right of current pointer index
    def remove(self):
        if (self.r_length() <= 0):
            print("No elements to remove/delete! Current is at the end of the list!")
        else:
            removed = self.Array[self.current]
            for i in range(self.current, self.length - 1):  # Elements from current pointer to end of array
                self.Array[i] = self.Array[i + 1]  # shifts one place to the left
            self.length -= 1
            print("Removed element with value: " + str(removed))

    # Print current element
    def print_current(self):
        if (self.r_length() <= 0):
            print("No elements to print! Pointer is at the end of the list!")
        else:
            print("Value of current element is: " + str(self.Array[self.current]))

    # Displaying/Printing all list elements
    def display(self):
        print("List length:" + str(self.length))
        # py doc --> range(start, stop, step)
        for i in range(0, self.length):
            print("Element " + str(i + 1) + " - position(" + str(i) + ") :" + str(self.Array[i]))

    # Displaying even elements
    def print_even(self):
        counter = 0
        print("List length:" + str(self.length))
        for i in range(0, self.length):
            if(self.Array[i] % 2 == 0):
                counter += 1
                print("Element " + str(counter) + " - position(" + str(i) + ") :" + str(self.Array[i]))
        print("Total even elements: " + str(counter))

    # Displaying odd elements
    def print_odd(self):
        counter = 0
        print("List length:" + str(self.length))
        for i in range(0, self.length):
            if (self.Array[i] % 2 != 0):
                counter += 1
                print("Element " + str(counter) + " - position(" + str(i) + ") :" + str(self.Array[i]))
        print("Total odd elements: " + str(counter))