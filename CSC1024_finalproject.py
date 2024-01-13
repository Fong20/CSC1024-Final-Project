# group project for team Psycho 

#Main Menu
import os
from datetime import datetime

#ASCII art
def menu_art():
  print('''
    __    __     ______     __     __   __         
   /\ "-./  \   /\  __ \   /\ \   /\ "-.\ \         
   \ \ \-./\ \  \ \  __ \  \ \ \  \ \ \-.  \      
    \ \_\ \ \_\  \ \_\ \_\  \ \_\  \ \_\\"\_ \      
     \/_/  \/_/   \/_/\/_/   \/_/   \/_/ \/_/      
    __    __     ______     __   __     __  __ 
   /\ "-./  \   /\  ___\   /\ "-.\ \   /\ \/\ \ 
   \ \ \-./\ \  \ \  __\   \ \ \-.  \  \ \ \_\ \ 
    \ \_\ \ \_\  \ \_____\  \ \_\\" \_\  \ \_____\ 
     \/_/  \/_/   \/_____/   \/_/ \/_/   \/_____/ 
  
  ''')
  print("\t\t  /////|\t |\\\\\\\\ ////|")
  print("\t\t ///// |\t | \\\\\\V/// |")
  print("\t\t|~~~|  |\t |  |~~~|  |")
  print("\t\t|===|  |\t |  |===|  |")
  print("\t\t|a  |  |\t |  |B  |  |")
  print("\t\t| r |  |\t |  | M |  |")
  print("\t\t|  t| /\t\t  \\ |  S| /")
  print("\t\t|===|/\t\t   \\|===|/")
  print("\t\t'___'\t\t    '---'")
  
#Relative file path. Open text file for read and write purpose.
#Exception handling (try and except) is used to handle IO Error.
try:
  with open ("books_StudentID.txt", "r+") as f:
    book_list = f.readlines()

except IOError:
  print("There is an error in reading from the text file!")

# Empty list for updating and editing of book information
updated_list = []
# Empty list for adding book information
add_list = []

#Main Menu of the program.
def main_menu():
  repeat = "YES"
  while repeat == "YES":
    menu_art()
    print("\nPersonal Book Management System\n")
    print("\n[1] Add Book Record(s)")
    print("[2] Delete Book Record(s")
    print("[3] Update / Edit Book Record(s)")
    print("[4] Display")
    print("[5] Search for Book(s)")
    print("[6] Exit")

    try:
      option = int(input("\nEnter the option from 1-6: "))

    except ValueError:
      print("\nINVALID entry, Option must be numerical! Please Try again.")
      option = int(input("\nEnter the option from 1-6: "))

    if option > 0 and option < 7:
      match option:
        case 1:
          add_book()
        case 2:
          delete_book()
        case 3:
          update()
        case 4:
          display()
        case 5:
          search()
        case 6:
          exit_program()
    else:
      print("\nOption must be from a numerical range of 1-6! Please Try again.")

#Display book information.
def display():
    #Display column headings
    print(f"\n{'ISBN' : <13}{'Author': ^30}{'Title': <100}{'Publisher': <30}{'Genre': <30}{'Year_Published': <20}{'Date_Published': <22}{'Status': <15}\n")
    
    #Display book information
    for i, book_data in enumerate(book_list):
      book_record = book_data.strip("\n").split(",")
      
      if len(book_record) >= 8:
        print(f"{book_record[0]: <13}{book_record[1]: ^30}"
            f"{book_record[2]: <100}{book_record[3]: <30}"
            f"{book_record[4]: <30}{book_record[5]: ^14}"
            f"{book_record[6]: ^26}{book_record[7]: ^10}")
    
    #Return to main menu
    cont = True
    while cont == True:
      choice = input("\nEnter 'Y' to return back to the main menu: ").upper()
      if choice != "Y":
        print("Invalid entry. Returning back to option again.")
      else:
        print('Returning to main menu...')
        cont = "False"
        main_menu()

#Add book information.
def add_book():
  print('''
                 .                    ..
              ......                 ....                          
           .............           .......         
         :....::.::::::::::.     ..........         
        .-.......::-:::::::..   ...::::::::-:......=     
        :-. ..:::.:::::::-:::. ....::::...---+.....=    
        --.....::..:.::---:::. ....::::...:--+.....=     
        --...:.:.::::::::::::. .....:::::..:--*....=;    
        +-.......::::::::::::. ....:::::...:--*....=:    
       .+:......::::::---::::. ....:::.:::...--+...=,     
       .=.......::.::::::::::. .....:::::....--+...=* 
       :=......:::.:::-::::::. ...:::::::....--+:..=.    
       :-......:.:::.::---:::. ....::::.....::--*..='     
       -:......::.::::---::::. ........::::.....:-=-;     
       =:.......:::::::---:::. ...::::.:.::::...:-==:    
       =..................::-. .:::......:......:-===     
       =..:-=-----:::::...:::: :::..::..::::......:-+     
      .=..::----=========---:: :::...............:-*     
         .=:=========--=\   ': :'   /=====-------+.     
                         lllllllllll

  ''')

  prompt = input("Welcome to the add book function.\nWould you like to add a new book? Use (Y) for yes and (N) for no: ").upper()
  #if the statement is true
  while True:
    if prompt == "Y":
      #creating a new list and adding books in accordingly
      new_book = [
        input("ISBN: "),   
        input("Author: "),
        input("Title: "),
        input("Publisher: "),
        input("Genre: "),
        input("Year Published (YYYY): "),
        input("Date Purchased (DD/MM/YYYY): "),
        input("Status (read/to-read/missing): "),
      ]
      
      while True:
        if len(new_book[0]) == 13 or new_book[0] == '' and new_book[0].isdigit():
            break
        else:
            print("ISBN should only have integers (0-9) and 13 digits only.")
            new_book[0] = input("ISBN: ")

      # limit user input to 4 digits
      while True:
        if len(new_book[5]) == 4 or new_book[5] == '' and new_book[5].isdigit():
            break
        else:
            print("Please enter 4 digits only (YYYY).")
            new_book[5] = input("Year Published (YYYY): ")

      while True:
        continuing = input("Would you like to add another book? (Y) for yes and (N) for no:").upper()

        #if the user did not use the given options, prompt the user to use only Y/N
        while continuing not in ["Y","N"]:
          continuing = input("Please enter Y/N only.").upper()

          #if user entered "Y" then import the add_book function
        if continuing == "Y":
          os.system('cls')
          add_list.append(new_book)
          print("Book added successfully")
          add_book()

        #if user entered "N" then return to the main menu
        elif continuing == "N":
          os.system('cls')
          add_list.append(new_book)
          print("Book added successfully")
          print("Returning to main menu")
          main_menu()
          break
          
    #if user enter "N" then return to the main menu
    elif prompt == "N":
      print("Returning to main menu...")
      main_menu()
      break

#Delete book information
def delete_book():
    print('''               
                               .-*@@%@@+              
                   :+#@#@%. :+#@@#=. =@@*             
                -*@%*-  :@@@@%+:  -*@@%+:             
                #@*  .=#@@#=. .=#@@#=.                
                 +@#%@%*-  -*%@%+-                    
              .=#@@#=. .=#@@#=.                       
           :+%@@*-  :+%@@*-                                                         
          =@@*  :+%@@*-                                  
         =@@#@@%+:                                     
          -#*=.                                        
             *@@@@@@@@@@@@@@@@@@@@@@@@@@@@@         
             =@@::::::::::::::::::::::::#@@         
             :@@:                       #@*         
              @@=   +%-    #%:    %%    @@=         
              #@*   =@*    %@:   .@%    @@:         
              +@@   -@#    %@:   -@#    =@@          
              -@@.  :@@    %@:   =@+    *@#          
              .@@-   @@    %@:   *@=    @@+          
               @@+   @@:   %@:   %@-   .@@-          
               #@#   #@-   %@:   @@.   -@@.          
               +@@   *@+   %@:   .@@   +@@           
               -@@.  +@*   %@:   :@%   #@#           
               .@@-  -@#   %@:   -@#   @@+           
                @@+  .++   ++.   :+-  .@@-           
                #@#                   -@@.           
                @@@@@@@@@@@@@@@@@@@@@@@@@            
                :::::::::::::::::::::::::
  
  ''')
    
    user_prompt = input("Do you wish to delete a book? Enter Y to delete a book and N to return to main menu: ").upper()

    #Exception handling using while loop
    while True:

        #If the user do not provide any option, prompt the user to re-enter an option.
        if user_prompt == "":
            user_prompt = input("\nPlease enter an option, y to delete book and n to return to main menu").upper()

        #If the user enters an option besides Y and N, prompt the user to enter only Y to delete book and N to return to main menu.
        elif user_prompt != "Y" and user_prompt != "N":
            user_prompt = input("\nPlease enter only Y to delete a book and N to return to main menu.").upper()

        #Proceed with following codes if all inputs are valid.
        else:
            break

    #User wishes to delete book.
    if user_prompt == "Y":

        #Exception handling is used to handle value error if user enters an input of string instead of integer.
        try:
            user_delete = int(input("\nPlease Enter the ISBN code of the book you would like to delete: "))

        except ValueError:
            print("\nInvalid isbn,isbn must be numerical!")
            user_delete = int(input("Please Enter the ISBN code of the book you would like to delete: "))

        #convert user input from integer into string.
        user_delete = str(user_delete)

        while True:
            #Indexing the book information based on each category.
            for book_data in book_list:
                data = book_data.split(",")
                isbn = data[0]

                #If the user's input matches the isbn of the book in the database, prompt user for confirmation if he/she wishes to delete book.
                if user_delete == isbn:
                    confirmation = input(f"Are you sure you want to delete the following book, {book_data}, Enter Y to continue or N to abort:").upper()

                    #Exception handling using while loop
                    while True:
                        if confirmation == "":
                            confirmation = input("Please enter an option, y to delete book and n to return to main menu").upper()

                        elif confirmation != "Y" and confirmation != "N":
                            confirmation = input("Please enter only Y to delete a book and N to return to main menu.").upper()

                        else:
                            break 

                    #If the user confirms to delete the book, remove the information of the book from the list
                    if confirmation == "Y":
                        book_list.remove(book_data)
                        print("\nThe Book has been deleted")
                        break
                        
                    
                    #If the user do not wish to proceed with the process of deleting the book, abort the process.
                    else:
                        print("\nThe Book Deletion process has been cancelled.")
                        break
                
                else:
                    os.system("cls")
                    print("\nSearching...")
                    
                
            #Prompt user if he/she wants to find another book.
            decision = input("\nWould you like to delete another book? Enter Y to delete another book and N to return to main menu: ").upper()

            #Exception handling using while loop
            while True:
                if decision == "":
                    decision = input("Please enter an option, y to delete book and n to return to main menu").upper()

                elif decision != "Y" and decision != "N":
                    decision = input("Please enter only Y to delete a book and N to return to main menu.").upper()

                else:
                    break

        
            #If user chooses to delete another book, the program prompts the user to enter another isbn info.
            if decision == "Y" :

                try:
                    user_delete = int(input("\nPlease Enter the ISBN code for the book you'd like to delete: "))

                except ValueError:
                    print("\nInvalid isbn,isbn must be numerical!")
                    user_delete = int(input("Please Enter the ISBN code for the book you'd like to delete: "))

                user_delete = str(user_delete)    


            #If user chooses not to delete another book, stop delete book process and return to main menu.
            else:
                break
        
        #Clear screen and exit to main menu
        os.system('cls')
        print("Thank you for using this function. Exiting to the main menu...")
        main_menu()

    #If user do not wish to delete books, the program will return to main menu.
    else:
        os.system('cls')
        print("Exiting to the main menu...")
        main_menu()

#Update book information.
def update():
  print('''
                         :%%%:          
                   =-.  .@@@@@:  :==    
                 .@@@@@@@@@@@@@@@@@@@.  
                  =@@@@@@@@@@@@@@@@@=   
                  :@@@@@@+---+@@@@@@-   
               +#@@@@@@%       #@@@@@@#+
               @@@@@@@@+       +@@@@@@@@
               .-=#@@@@@=     =@@@@@#=: 
                  .@@@@@@@%#%@@@@@@@.   
                  #@@@@@@@@@@@@@@@@@%   
                  =@@#+=#@@@@@#=+#@@+   
                         *@@@#    
  ,--. ,--.,------. ,------.    ,---. ,--------.,------. 
  |  | |  ||  .--. '|  .-.  \  /  O  \'--.  .--'|  .---' 
  |  | |  ||  '--' ||  |  \  :|  .-.  |  |  |   |  `--,  
  '  '-'  '|  | --' |  '--'  /|  | |  |  |  |   |  `---. 
   `-----' `--'     `-------' `--' `--'  `--'   `------'                     
                                                          ''')

  while True:  
      count = 0
      Modified_book = []
      
      # splitting the index and extract the book title from the list 
      for book_data in book_list:
          line = book_data.split(",")

          # list out the books 
          if (len(line) >= 8 and line[2] != [] ):
              count += 1
              print(f"{count}) {line[2]}") 

      # prompt user to select a book to update
      while True:  
          try:
              book_choice = int(input("Please select the book that you wish to edit (1/2/3 etc.):"))

              if 1 <= book_choice <= len(book_list): # to check of the number is within range
                  selected_book = book_list[book_choice - 1] # minus 1 because index start from 0
                  print("You selected:", selected_book)
                  Modified_book = selected_book.split(",")
                  break 
              else :
                  print("Number out of range!")

      # to make sure that user enter same format as given
          except ValueError:
              print("Please enter displayed numbers only without spacing and symbols.")

      # prompt user to enter parts that need to edit
      # if nothing entered then it will remain the same
      print("Please enter new info for required section.")
      print("If you wish to keep the original info, leave it blank and proceed.")

      # isdigit() is used to check if the user enter digits only(0-9)
      # if the user leave it blank, it will keep original content
      isbn = input("ISBN:")
      while not (isbn == '' or (len(isbn) == 13 and isbn.isdigit())):
          print("Please enter a valid ISBN with 13 digits:")
          isbn = input("ISBN:")

      # no restriction because each book is different
      author = input("Author:")
      title = input("Title:")
      publisher = input("Publisher:")
      genre = input("Genre:")

      # only 4 digits number allowed
      yearPublished = input("Year Published (YYYY):")  
      while not (yearPublished == '' or (len(yearPublished) == 4 and yearPublished.isdigit())):
          print("Please enter a valid year(YYYY).")
          yearPublished= input("Year Published (YYYY):")

      # restricting user input for date
      while True:
          try:
              datePurchased = input("Date Purchased (DD/MM/YYYY):")
              if (datePurchased != ''):
                  day, month, year = [int(item) for item in datePurchased.split('/')]
                  purchased_date = datetime(year, month, day).strftime('%d-%m-%Y')
                  purchased_date = purchased_date.replace('-', '/')
                  break

              else:
                  break
          except ValueError:
              print("Please enter a valid date according to the format given (DD/MM/YYYY).")

      status = input("Status (read/to-read/missing):")

      # nested if statements used to check user input and decide the final book info
      while True:

          # if isbn is not empty and valids it will append into list
          if isbn != "":
              Modified_book[0] = isbn

          # if author is not empty and valids it will append into list
          if author != "":
              Modified_book[1] = author

          # if title is not empty and valids it will append into list
          if title != "":
              Modified_book[2] = title

          # if publisher is not empty and valids it will append into list
          if publisher != "":
              Modified_book[3] = publisher

          # if genre is not empty and valids it will append into list    
          if genre != "":
              Modified_book[4] = genre

          # if yearPublised is not empty and valids it will append into list  
          if yearPublished != "":
              Modified_book[5] = yearPublished

          # if datePurchased is not empty and valids it will append into list
          if datePurchased != "":
              Modified_book[6] = purchased_date

          # if status is not empty and valids it will append into list
          if status != "":
              Modified_book[7] = status

          break

      print("Info Updated!")

      # ask if user wanted to continue
      repeat = input("Do you wish to edit another book? Y for yes, N for no:").upper()

      # restrict user input
      while repeat not in ["Y", "N"]:
          repeat = input("Please enter Y or N only:").upper()

      # if y is entered, clear the panel and start again
      if repeat == "Y":
          os.system('cls')
          updated_list.append(Modified_book)
          update()
      # if n is entered, clear the panel and return to main menu
      if repeat == "N":
          os.system('cls')
          updated_list.append(Modified_book)
          print("\nReturning to main menu.")
          main_menu()

      break




#Search function used to search for the information of the book based on the user's input.
def search():
  print('''
                                      -*#@@#+-
                            _      .*@@      @@*. 
                           | |     =@@         @@=  
    ___  ___  __ _ _ __ ___| |__    *@@       @@%
   / __|/ _ \/ _` | '__/ __| '_ \     .+%@++@=@
   \__ \  __/ (_| | | | (__| | | |          .%@#:
   |___/\___|\__,_|_|  \___|_| |_|            %@@:
''')

  #Double confirm with user if he/she wants to search for a book.
  user_confirmation = input("Do you want to search for a book? Enter Y to search for a book or N to return to main menu.").upper()

  #Exception handling using while loop
  while True:
    
    #When user did not choose an option to find a book, it will request user to re-enter the specific input.
    if user_confirmation == "":
      user_confirmation = input("\nPlease enter an option, Y to continue searching for another book or N to return to main menu:").upper()

    #When user enters any input besides "Y" and "N", it will request user to re-enter the specific input.
    elif user_confirmation != "Y" and user_confirmation != "N":
      user_confirmation = input("\nPlease enter only Y to continue searching for another book or N to return to main menu:").upper()

    #If there are no issues, break out from the infinite loop and continue with the following codes.
    else:
      break

#User wishes to search for a book.
  if user_confirmation == "Y":
  
    while True:

      #Prompt user to entter information of book
      #Exception handling is used to prevent user from entering string for isbn
      try:
        isbn = int(input("\nPlease enter the ISBN:"))
      
      except ValueError:
          print("Invalid isbn, isbn must be numerical")
          isbn = int(input("\nPlease enter the ISBN:"))

      #Convert isbn from integer into string
      isbn = str(isbn)
      author = input("Please enter the author:")
      title = input("Please enter the title:")

      #If user do not enter author or title, prompt user to re-enter book information.
      if author == "" or title == "":
        print("\nPlease enter the required ISBN, author and title of the book")  

      #If user enters isbn, author and title correctly, proceed with following codes
      else:
        break


    while True: #Infinite loop

      for book_data in book_list:

    #Indexing of book information based on each category (isbn, author and title)
        #Split each information of the book in string into a list using comma (split)
        book_index = book_data.strip("\n").split(",")

        if len(book_index) >= 8:
          #Assign isbn information of the book into a single variable named isbn_index
          isbn_index = book_index[0].lower()

          #Assign author information of the book into a single variable named author_index
          author_index = book_index[1].lower()

          #Assign title information of the book into a single variable named tltle_index
          title_index = book_index[2].lower()

    #Search for the information of the book
        #If the user's input of book information is found, display the information of the book and stop searching.
        if isbn == isbn_index and author == author_index and title == title_index:
          print("\nHere is the information of the book:\n", book_data)
          books_found = True
          break

        #If the book is not found, continue searching.
        else:
          books_found = False


      #Control statement using user's input
      #Once the information of the book is displayed, prompt user if they wish to find another book.
      if books_found == True:
        decision = input("Would you like to find another book? Enter Y to search for another book or N to return to main menu:").upper()
      
      #If the information of the book is still not found after searching whole database, prompt user if they wish to find another book.
      else:
        print("\nSorry, the information of the book is not found")
        decision = input("Would you like to find another book? Enter Y to search for another book or N to return to main menu:").upper()

      #Exception handling using while loop. 
      while True: 
        #When user did not choose an option to continue or exit program, it will request user to re-enter the specific input
        if decision == "":
          decision = input("\nPlease enter an option, Y to continue searching for another book or N to return to main menu:").upper()

        #When user enters any input besides "Y" and "N", it will request user to re-enter the specific input.
        elif decision != "Y" and decision != "N":
          decision = input("\nPlease enter only Y to continue searching for another book or N to return to main menu:").upper()

        else:
          break


      #When user inputs Y, the system will prompt user to enter new book information
      if decision == "Y":

        while True:
          
          #Prompt user to entter information of book
          #Exception handling is used to prevent user from entering string for isbn
          try:
            isbn = int(input("\nPlease enter the ISBN:"))
          
          except ValueError:
              print("Invalid isbn, isbn must be numerical")
              isbn = int(input("\nPlease enter the ISBN:"))

          #Convert isbn from integer into string
          isbn = str(isbn)
          author = input("Please enter the author:")
          title = input("Please enter the title:")

          #If user do not enter author or title, prompt user to re-enter book information.
          if author == "" or title == "":
            print("\nPlease enter the required ISBN, author and title of the book")  

          else:
            break

      #When user inputs N, it will exit the system and return to main menu
      else:
        break


  #clear terminal and return to main menu  
    os.system('cls')
    print("Returning to main menu...")
    main_menu()

#User do not wish to search for a book.
  else:
    os.system('cls')
    print("Returning to main menu...")
    main_menu()

#Exit program.
def exit_program():
  print('''
                          =#*=-.                  
               :==========*######*.               
               -=         =#######.               
               -=         =#######.               
               -= -++-    =#######.               
               -=.###%:   =#######.               
            :--==:-==:    =#######.               
          :*#+=+%###+     =#######.               
          ++.  =#####*... =#######.               
               #### =###*:=#######.               
              +###-       =#######.               
            :*#++##-      =#######.               
      #######*:-= +##     =#######.               
               -= :##     =#######.               
               -= :##     =#######.               
               -= .#*     =#######.               
               :===--=====*######*.               
                          =#-=*'
  
  ''')

  #Relative file path. Open text file in write mode.
  with open ("books_StudentID.txt", "w") as f:

    #Double confirm with user to exit the program
    user_confirmation = input("Do you wish to exit the program? Enter Y to exit or N to return to main menu:").upper()

    #Exception handling using while loop. 
    while True:

      #When user did not choose an option to continue or exit program, it will request user to re-enter the specific input.
      if user_confirmation == "":
        user_confirmation = input("\nPlease enter an option, Y to exit the program or N to return to main menu:").upper()

      #When user enters any input besides "Y" and "N", it will request user to re-enter the specific input.
      elif user_confirmation != "Y" and user_confirmation != "N":
        user_confirmation = input("\nPlease enter only Y to exit the program and N to return to main menu:").upper()

      #If user provides correct input, proceed with following codes
      else:
        break

  #User confirms to exit the program
    if user_confirmation == "Y":

    #Write deleted book information into text file.
      for book_data in book_list:
        f.write(book_data)

    #Write updated book information and new book information into text file.
    #Since there are two lists, nested .join() is used to join the elements of each list into string.
      updated_bookinfo = "\n".join(",".join(update_info) for update_info in updated_list)
      added_bookinfo = "\n".join(",".join(add_info) for add_info in add_list)

      f.write(updated_bookinfo)
      f.write(added_bookinfo)

    #clear screen, inform the user that book information has been updated and exit the program.
      os.system('cls')  
      print("Your updated information has been saved, Thank you for using the program.")
      exit()
      
  #User do not wish to exit the program, clear screen and return to main menu.
    else:
      os.system('cls')
      print("Returning to main menu...")
      main_menu()
  
    
main_menu()