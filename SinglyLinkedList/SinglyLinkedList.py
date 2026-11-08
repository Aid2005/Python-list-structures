# *** SINGLY LINKED LISTS ***

class Node():
    # Node class - basic building element for all data structures
    def __init__(self, element=None):
        self.element = element
        self.next = None

    def __str__(self):
        return str(self.element)


class SinglyLinkedList():
    # Class defining the Singly Linked List structure using Node structure
    # Capacity :: "UNLIMITED"
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None
        self.r_length = 0
        self.l_length = 0

    # Move to start
    def move_to_start(self):
        self.current = self.head
        self.r_length += self.l_length
        self.l_length = 0
        print("Current pointer set to START of the list!")

    # Move to end
    def move_to_end(self):
        self.current = self.tail
        self.l_length += self.r_length
        self.r_length = 0
        print("Current pointer set to END of the list!")

    # Move to next
    def move_to_next(self):
        if (self.r_length != 0):
            if (self.current == None):  # Current is not set!
                self.current = self.head
                print("Pointer set to START of the list!")
            else:
                self.current = self.current.next
            self.l_length += 1
            self.r_length -= 1
            print("Current pointer set to NEXT element of the list!")
        else:
            print("Current pointer is at the end of the list!")

    # Move to previous
    def move_to_previous(self):
        if (self.l_length != 0):
            if (self.l_length == 1):
                self.current = self.head
                print("Pointer set to START of the list!")
            else:
                temp = self.head
                while (temp.next != self.current):
                    temp = temp.next
                self.current = temp
                print("Current pointer is set to PREVIOUS element of the list!")
            self.l_length -= 1
            self.r_length += 1
        else:
            print("Current pointer is at the start of the list!")

    # Move to custom position (left)
    def move_to_position(self, position):
        if ((position < 0) or (position > (self.l_length + self.r_length))):
            print("Given position is out of range!")
        else:
            self.r_length = self.r_length + self.l_length - position
            self.l_length = position
            if (position == 0):
                self.current = self.head
                print("Current pointer points to START of the list")
            else:
                self.current = self.head
                for i in range(0, position - 1):
                    self.current = self.current.next
            print("Current pointer set to position:" + str(position))

    # Adding elements to the end
    def add(self, x):
        new_node = Node(x)

        if (self.r_length + self.l_length == 0):  # If Singly Linked List is empty
            self.head = new_node
            self.tail = new_node
            print("List was empty. Start and end of the list are now the same new node!")
        else:  # If Singly Linked List is not empty
            self.tail.next = new_node  # Current tail node sets next pointer to new node
            self.tail = new_node  # Tail pointer moves to new node at the end of the list
            print("Successfully added element to the end of the list!")

        self.r_length += 1

    # Inserting element at current position (additional element on right partition)
    def insert(self, x):
        temp = Node(x)

        if (self.l_length == 0):
            temp.next = self.head
            self.head = temp
            if (self.l_length + self.r_length == 0):
                self.tail = temp
            print("Successfully inserted element " + str(x) + " at start of the list")
        else:
            temp.next = self.current.next
            self.current.next = temp
            if (self.r_length == 0):
                self.tail = self.current.next  # temp
            print("Successfully inserted element " + str(x) + " at pointer position " + str(self.current))

        self.r_length += 1

    # Removing/Deleting current element - first element of the right partition
    def remove(self):
        if (self.r_length <= 0):
            print("No elements to remove/delete! Current is at the end of the list!")
        else:
            temp = Node()

            if (self.l_length == 0):  # Current at start of the list
                temp = self.head
                self.head = temp.next
                print("Element removal completed!")
            else:
                temp = self.current.next  # Current in middle of the list
                self.current.next = temp.next
                print("Element removal completed!")

            if (self.r_length == 1):  # Current one element before end of list
                self.tail = self.current

            self.r_length -= 1

    # Print current element (left)
    def print_current(self):
        if (self.r_length == 0):
            print("No elements to print! Pointer is at the end of the list!")
        elif (self.current == None):
            print("Value of element at start of list is: " + str(self.head.element))
        else:
            print("Value of element at current position is: " + str(self.current.element))

    # Displaying/Printing all list elements
    def display(self):
        if (self.r_length + self.l_length == 0):
            print("List is empty!")
        else:
            temp = self.head
            counter = 0

            while (temp != None):
                print(str(counter) + ": " + str(temp), end="")

                # Additional pointers on display
                if (temp == self.head):
                    print(" <- start", end="")
                if (temp == self.current):
                    print(" <- current", end="")
                if (temp == self.tail):
                    print(" <- end", end="")
                print("")

                temp = temp.next
                counter += 1

    def print_even(self):
        if (self.r_length + self.l_length == 0):
            print("List is empty!")
        else:
            temp = self.head
            counter = 0

            while (temp != None):
                if (int(temp.element) % 2 == 0):
                    counter += 1
                    print(str(counter) + ": " + str(temp.element), end="")

                    # Additional pointers on display
                    if (temp == self.head):
                        print(" <- start", end="")
                    if (temp == self.current):
                        print(" <- current", end="")
                    if (temp == self.tail):
                        print(" <- end", end="")
                    print("")

                temp = temp.next

            print("Total even elements: " + str(counter))

    def print_odd(self):
        if (self.r_length + self.l_length == 0):
            print("List is empty!")
        else:
            temp = self.head
            counter = 0

            while (temp != None):
                if (int(temp.element) % 2 != 0):
                    counter += 1
                    print(str(counter) + ": " + str(temp.element), end="")

                    # Additional pointers on display
                    if (temp == self.head):
                        print(" <- start", end="")
                    if (temp == self.current):
                        print(" <- current", end="")
                    if (temp == self.tail):
                        print(" <- end", end="")
                    print("")

                temp = temp.next

            print("Total odd elements: " + str(counter))

    def difference(self):
        if (self.r_length + self.l_length == 0):
            print("List is empty!")
        else:
            temp = self.head
            ecounter = 0
            ocounter = 0

            while (temp != None):
                if (int(temp.element) % 2 != 0):
                    ocounter += 1
                else:
                    ecounter += 1

                temp = temp.next

            print("Even elements count " + str(ecounter) + ", and odd elements count " + str(ocounter))
            if (ecounter > ocounter):
                print("There are more even elements!")
            elif (ecounter < ocounter):
                print("There are more odd elements!")
            else:
                print("Count is equal!")