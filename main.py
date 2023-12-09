# ******* run this File *******

from database import db
from functions import *


while True:
    # show menu
    print("""
          1 - add new entries
          2 - remove entries
          3 - edit entries
          4 - search entries
          5 - display entries
          """)
    select = input("choice a option:")
    
    # add product or category
    if select == "1":
        print("1- product\n2 - category")
        which = input("select a section: ")
        if which == "1":
            add_product()
        elif which == "2":
            add_category()
        else:
            print("not found!")
            
    # remove product or category     
    elif select == "2":
        print("1- product\n2 - category")
        which = input("select a section: ")
        if which == "1":
            remove_product()
        elif which == "2":
            remove_category()
        else:
            print("not found!")
            
    # update product or category
    elif select == "3":
        print("1- product\n2 - category")
        which = input("select a section: ")
        if which == "1":
            update_product()
        elif which == "2":
            update_category()
        else:
            print("not found!")
            
    # search product or category
    elif select == "4":
        print("1- product\n2 - category")
        which = input("select a section: ")
        if which == "1":
            search_product()
        elif which == "2":
            search_category()
        else:
            print("not found!")
            
    # display product or category
    elif select == "5":
        print("1- product\n2 - category")
        which = input("select a section: ")
        if which == "1":
            display_product()
        elif which == "2":
            display_category()
        else:
            print("not found!")
            
    # exit
    elif select == "6":
        print("good luck :)")
        break
    
    # not found selector
    else:
        print("not found!")
            
    
    
            
