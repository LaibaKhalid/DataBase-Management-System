import mysql.connector
from tabulate import tabulate

mydb = mysql.connector.connect(host='localhost',                           #mydb is connection object
                               user='root',
                               password='Psycho786pass',
                               port='3306',
                               database='engineering_projects')

mycursor = mydb.cursor()                           #mycursor is the variable created, using which we can use different commands
                                                    #use mycursor.execute to write Sql code in it-- can also create a table
                                              #for loop(i.e., looping through the table
                                            #user (or any other name x) is just an iterable object/variable using which
                                             #we are printing all values from our table employee

                                        #example of a table creation:
                                        #mycursor.execute("CREATE TABLE employees (E_name VARCHAR(50),
                                        #E_age smallint UNSIGNED, E_id int PRIMARY KEY AUTO_INCREMENT)")

    #commit() to reflect changes made here on the database





def selection(query, header):                                  #for indexing and selecting data  (returns the name of the table chosen)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    result= mycursor.fetchall()
    print()
    print("Available", header, ":-")
    for i in range(len(result)):
        index = i + 1
        print(f"{index}. {result[index - 1][0]}")
    print()
    if header == "Tables":
        choice = input("Select your choice in numbers: ")
        if len(choice) == 0 or int(choice) > index or int(choice) < 1:
            print("Invalid choice!")
            return None
        return result[int(choice) - 1][0]




def showtc():                                                    # To show available tables and columns in the database
    table = selection("show tables", "Tables")
    if table is None:
        return
    selection("show columns from " + table, "Columns")
    return table



def wait():                                      # To pause execution
    print()
    choice = input("Continue(Y/N)? ")
    if choice != "Y" and choice != "y":
        print()
    exit()


def run(query):                                     # Runs queries to modify the contents of the database
    try:
        mycursor = mydb.cursor()
        mycursor.execute(query)
        mydb.commit()
        print("Sucessful commit")
        wait()


    except:
        print('Invalid query!')
        print()
        mydb.rollback()


def insert_data():                                         # To insert data in a table
    table = showtc()
    if table is None:
        return

    print("Enter data to be inserted in the form ('abc',45,'917-19-10','abde',....)")
    q = input()
    query = "insert" + " into " + table + " values " + q
    run(query)



def update_data():                                                       # To update data in a table
    table = showtc()
    if table is None:
        return
    print("Enter query in the form of 'set column_name = 'value' where 'condition' ' ")
    q = input()
    query = "update" + " " + table + " " + q
    run(query)


def delete_data():                                                  # To delete data from a table
    table = showtc()
    if table is None:
        return

    print("Enter condition")
    q = input()
    query = "delete" + " from " + table + " where " + q
    run(query)


def display_table(table):                                         # To display the contents of a table (in atbular form)
    mycursor = mydb.cursor()
    query = "select * from " + table
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    print(tabulate(myresult, headers=[i[0] for i in mycursor.description],
                   tablefmt='fancy_grid'))
    wait()


def create_table():                                              # To create a new table in the database
    print("Write a one-line query :-")
    q = "create table "
    query = input(q)
    query = q + query
    run(query)
    return



def alter_table():                                                    # To alter the contents of the table
    table = selection("show tables", "Tables")
    print("Complete query :-")
    q = "alter table " + table + " "
    query = input(q)
    query = q + query
    run(query)


def drop_table():                                                     # To delete an already existing table
    table = selection("show tables", "Tables")
    query = "drop table " + table
    run(query)


def menu():                                           # Displays available options in the database
    print()
    print("************************\n")
    print("\t TABLE MENU \t")
    print(" 1. Show all tables and columns \n 2. Display a table \n 3.Create new table \n 4.Delete existing table \n 5.Alter table")
    print("************************")
    print("\t DATA MENU \t")
    print(" 6. Insert data \n 7. Delete data \n 9. Update data \n 10. Exit")
    print("\n************************")
    print()


def main():                                                       # Main program function providing choices for the menu

    print("\t Welcome to ENGINEERING PROJECTS DATABASE \t")

    while True:

        menu()
        choice = int(input("Enter choice (1 - 10): "))

        if choice == 1:
            showtc()

        elif choice == 2:
            table = selection("show tables", "Tables")
            display_table(table)

        elif choice == 3:
            create_table()

        elif choice == 4:
            drop_table()

        elif choice == 5:
            alter_table()

        elif choice == 6:
            insert_data()

        elif choice == 7:
            delete_data()

        elif choice == 8:
            update_data()

        elif choice == 9:
            break

        else:
            print("not a valid input"+"\n choose from the given options")
            wait()
            continue


main()                                                 # Calling the main fuction and executing the program for database





