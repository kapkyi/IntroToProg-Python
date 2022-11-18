# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Kapkyi Lwai,11/15/2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = None  # object that represent a file
strFile = 'ToDoList.txt'
lstRow = ''  # A row of text data from the file
dicRow = {'Task', 'Priority'}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ''  # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile = open(strFile, 'w')
objFile = open(strFile, 'r')
for row in objFile:
    lstRow = row.split(',')
    dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()}  # Add list data to dictionary
    lstTable.append(dicRow)  # dictionary to table
objFile.close()  # close file

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print('''
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    ''')
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('Task' + ', \t' + 'Priority(low 1-5 high)')
        for row in lstTable:
            print(row['Task'], row['Priority'], sep=', ')
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):

        print('Type in a task and its priority.')
        strTask = input('Enter a Task: ')
        strPriority = input('Enter its Priority (low 1-5 high): ')
        dicRow = {'Task': strTask, 'Priority': strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):

        print(lstTable)  # Display the list to user for reference
        strRemove = input('Enter a task to be removed: ')
        for row in lstTable:
            if row['Task'].lower() == strRemove.lower():
                lstTable.remove(row)
                print(strRemove.title() + ' task is removed')
            else:
                print(strRemove.title() + 'is invalid input (not on your todo list)')    #display user input data does not exist
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open('ToDoList.txt', 'w')  # open file in write mode
        for Row in lstTable:
            objFile.write(Row['Task'] + ',' + Row['Priority'] + '\n')  # write lstTable items to file
        objFile.close()
        print('Data Saved to File!')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):

        print('Thank you come again!')
        break  # and Exit the program
