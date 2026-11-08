import sys
from SinglyLinkedList import SinglyLinkedList


def display_menu():
    print("\n     ** TEST PROGRAM FOR SinglyLinkedList **")
    print("-------------------Menu--------------------")
    print("1.  Go to previous")
    print("2.  Go to next")
    print("3.  Go to start")
    print("4.  Go to end")
    print("5.  Go to position")
    print("6.  Add element to end of list")
    print("7.  Insert element at current position")
    print("8.  Remove current element")
    print("9.  Print current element value")
    print("10. Display list contents")
    print("11. Print even elements")
    print("12. Print odd elements")
    print("13. Print difference between even and odd elements")
    print("99. Exit")
    print("----------------------------------------------------")


def main():
    my_list = SinglyLinkedList()

    while True:
        display_menu()
        try:
            choice = int(input("Select an option: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        match choice:
            case 1:
                my_list.move_to_previous()
            case 2:
                my_list.move_to_next()
            case 3:
                my_list.move_to_start()
            case 4:
                my_list.move_to_end()
            case 5:
                try:
                    position = int(input("Enter position to move current pointer:\n"))
                    my_list.move_to_position(position)
                except ValueError:
                    print("Position must be an integer!")
            case 6:
                try:
                    value = int(input("Enter element value to add:\n"))
                    my_list.add(value)
                except ValueError:
                    print("Value must be an integer!")
            case 7:
                try:
                    value = int(input("Enter element value to insert:\n"))
                    my_list.insert(value)
                except ValueError:
                    print("Value must be an integer!")
            case 8:
                my_list.remove()
            case 9:
                my_list.print_current()
            case 10:
                print("\n** LIST ELEMENTS **")
                my_list.display()
            case 11:
                my_list.print_even()
            case 12:
                my_list.print_odd()
            case 13:
                my_list.difference()
            case 99:
                print("Program terminated!\n")
                sys.exit()
            case _:
                print("Invalid choice. Please try again!")


if __name__ == "__main__":
    main()