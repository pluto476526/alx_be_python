# Using lists to store and manipulate data

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to list.")
        elif choice == '2':
            item = input("Enter the item to remove: ")
            if item not in shopping_list:
                print(f"{item} not found.")
            else:
                shopping_list.remove(item)
                print(f"{item} has been removed.")
        elif choice == '3':
            if shopping_list:
                print("Your shopping list:")
                for item in shopping_list:
                    print(item)
            else:
                print("Shopping list empty")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
