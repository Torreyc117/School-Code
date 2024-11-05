import sqlite3

#create database
CONNECTION = sqlite3.connect('demo.sqlite3')

#instantia a cursor object
cursor = CONNECTION.cursor()

#create table
cursor.execute('DROP TABLE IF EXISTS Assignments')
cursor.execute('CREATE TABLE Assignments (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(25),description VARCHAR(200))')

#------------
def printAssignments():
    cursor = CONNECTION.cursor ()
    # execute the SQL query using execute() method.
    cursor.execute("SELECT title, description from Assignments")
    print("\n-----Current Assignments-----")
    for row in cursor:
        print (row[0] + " - " + row[1])
    cursor.close()
    print("-----------------------------")

def createAssignment():
    title = input("Enter an assignment title: ")
    description = input("Enter an assignment description: ")
    
    #to do: create a cursor from the CONNECTION
    cursor = CONNECTION.cursor()
    #to do: execute a SQL statement to insert a new Assignment record based on the title and description entered by the user
    cursor.execute('INSERT INTO Assignments (title, description) VALUES (?,?)', (title, description))
    #to do: commit the delete to the database
    CONNECTION.commit()
    #to do: close the cursor object
    cursor.close()
def deleteAssignmentByTitle():
    #to do: use the input function to obtain an assignment title to delete from the Assignment table
    title = input("Enter an assignment title: ")
    #to do: create a cursor from the CONNECTION
    cursor = CONNECTION.cursor()
    #to do: execute a SQL statement to delete the Assignment based on the title entered by the user
    cursor.execute('DELETE FROM Assignments WHERE title = ?', (title,))
    #to do: commit the delete to the database
    CONNECTION.commit()
    #to do: close the cursor object
    cursor.close()
    print("Assignment successfully deleted.")
    
def exportAssignmentsToFile():
    #to do: create a cursor from the CONNECTION
    cursor = CONNECTION.cursor()
    #to do execute a SQL SELECT query using execute() method.
    cursor.execute("SELECT title, description from Assignments")
    
    #to do: open a file writing
    myFile = open("ExportFile.txt","w")
    #to do: similar to the printAssignments function, use a for loop to iterate each row and write the title and description columns to the file.
    #each title and description must be on a seperate row in the file output
    for row in cursor:

        myFile.write(row[0] + " - " + row[1] + "\n")
    #to do: close the cursor object
    cursor.close()
    #to do: close the file object
    myFile.close()
    print("Export Complete.")
    
def showMenu():
    selection = ""
    while selection != "5":
        print("\n*************MENU*************")
        print("1 - Create Assignment")
        print("2 - Delete Assignment By Title")
        print("3 - Print Assignments to Screen")
        print("4 - Export Assignments to File")
        print("5 - Quit")
        print("")
        selection = input("Please enter a menu number: ")
        
        if selection == "1":
            createAssignment()
        if selection == "2":
            deleteAssignmentByTitle()
        if selection == "3":
            printAssignments()
        if selection == "4":
            exportAssignmentsToFile()
        if selection == "5":
            CONNECTION.close()
        
showMenu()