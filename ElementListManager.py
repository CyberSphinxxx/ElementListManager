element_list = []
separator = "-------------------------------------------------------------------------------------------------"

while True:
    print(separator)
    print("Current elements in the list:", element_list)
    print(separator)
    print("\nEnter 'a' to add a new element, 'r' to remove an element, 'p' to print elements, or 'q' to quit")
    choice = input("Enter Choice: ")

    if choice.lower() == 'a':
        element = input("Enter the element to add: ")
        element_list.append(element)
        print(f"Element '{element}' added successfully!")
        
    elif choice.lower() == 'r':
        if element_list:
            element_to_remove = input("Enter the element to remove: ")
            if element_to_remove in element_list:
                element_list.remove(element_to_remove)
                print(f"Element '{element_to_remove}' removed successfully!")
            else:
                print("Element not found in the list!")
        else:
            print("The list is empty. Nothing to remove.")
            
    elif choice.lower() == 'p':
        print("Printing elements in the list:")
        for element in element_list:
            print(element)
            
    elif choice.lower() == 'q':
        print("Exiting program...")
        break
        
    else:
        print("Invalid choice! Please enter 'a' to add, 'r' to remove, 'p' to print, or 'q' to quit.")
