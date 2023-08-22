# V 3.2.0

import books_operations as bo

#--------------------- Main --------------------
while True:
    bo.clear()
    print("=================================")
    print("Press A to add a book")
    print("Press L to list all book")
    print("Press F to find a book")
    print("Press D to delete a book")
    print("Press S to save all books")
    print("Press Q to quit application")
    print("=================================")
    choice = input("Enter Your Choice : ").upper()
    if   choice == 'A' :
        bo.add_book()
    elif choice == 'L' :
        bo.list_books()
    elif choice == 'F' :
        bo.find_book()
    elif choice == 'D':
        bo.delete_book()
    elif choice == 'S':
        bo.save_books()
    elif choice == 'Q' :
        break
    else : input("\n\nWrong Choice ! Press any key ...")