#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Sayali , 2022-Feb-27, Completed the Todo and Assignemnts
#------------------------------------------#
# Declare variabls
strChoice = '' # User input
lstTbl = []  # list of lists to hold data # DONE replace list of lists with list of dicts
lstRow = []  # list of data row
dicRow = {}
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()
    if strChoice == 'x':
        # 1. Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # DONE Add the functionality of loading existing data
        # 2. Load exiting data in the memory
        lstTbl.clear()
        objfile = open(strFileName, 'r')
        for each in objfile:
            lst1 = each.strip().split(',')
            dicRow = {'strID' :lst1[0],'strTitle': lst1[1], 'strArtist' :lst1[2]}
            lstTbl.append(dicRow)
        objfile.close()
    if strChoice == 'a':  # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 3. Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intId = int(strID)
        dicRow = {'strID':intId,'strTitle' :strTitle, 'strArtist': strArtist }
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 4. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(*row.values(), sep = ', ')
    elif strChoice == 'd':
        # 5. Delete the entry from the table (ID/ArtistName/ArtistTitle)
        # DONE Add functionality of deleting an entry
        entry_input = input("Enter the ID Value,Artistname or Artist title to delete: ")
        print('Entry input is', entry_input)
        if lstTbl == []:
            print("Cannot delete as no data in 2D table")
        else:
            for item in lstTbl:
                if entry_input in item.values():
                    lstTbl.remove(item)
    elif strChoice == 's':
        # 6. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            for item in row.values():
                strRow += str(item) + ','
            strRow = strRow[:-1] + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        # 7. Please slect the valid input from Menu
        print('Please choose either l, a, i, d, s or x!')

