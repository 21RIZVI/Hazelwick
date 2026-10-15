list =[]
option = 0
print("----shopping list----")
while option != 5:
    print ("1. Add an item")
    print ("2.Remove an item")
    print ("3. View the list")
    print ("4. Count items")
    print ("5. Quit")
    print()
    option = int(input("choose an option:"))
    if option == 1:
        item_added = input("Item to add:")
        list.append(item_added)
        print(item_added ,"added")
        print()
    elif option == 3:
        print(list)
    elif option == 2:
        print(list)
        destroy = input("choose an item to remove:")
        list.remove(destroy)
    elif option == 4:
        total = len(list)
        print(total)
        print()
    elif option > 5:
        print("invalid option,please choose 1-5")
        print()