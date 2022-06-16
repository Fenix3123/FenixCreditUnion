import csv
import mysql.connector
from collections import Counter
from dotenv import load_dotenv
import os
load_dotenv()

#connects to mysql 
db = mysql.connector.MySQLConnection(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database="hw2"
)
#Classes
class user:
    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role

class address:
    def __init__(self, user_ID, address_line, city, country, zipcode):
        self.address_line = address_line
        self.city = city
        self.country = country
        self.zipcode = zipcode
        self.user_ID = user_ID

class bank:
    def __init__(self, user_ID, balance):
        self.balance = balance
        self.user_ID = user_ID

list1 = []        

#creates stuff and puts it in the table
def insert_user(newUser):
    try:
        #insert users
        mycursor = db.cursor()
        sql_user_insert = """INSERT INTO users (name, username, password, role) VALUES('{}','{}','{}', '{}')""".format(newUser.name,newUser.username,newUser.password,newUser.role)
        mycursor.execute(sql_user_insert)
        db.commit()
        #selecting user
        result = get_user(newUser.username)
            #creating bank object
        bank_account = bank(result[0], 0)
        sql_bank = """INSERT INTO bank_accounts (balance, user_ID) VALUES('{}','{}')""".format(bank_account.balance, bank_account.user_ID)
        mycursor.execute(sql_bank)   
        db.commit()
        #insert into address
            #creating address object
        user_address = address(result[0], None, None, None, None)
        sql_user_address_insert = """INSERT INTO address (address_line, city, country, zipcode, user_ID) VALUES('{}','{}','{}','{}','{}')""".format(user_address.address_line, user_address.city, user_address.country, user_address.zipcode, user_address.user_ID)
        mycursor.execute(sql_user_address_insert)
        db.commit()
        print("successful inserted")
    except mysql.connector.Error as e:
        print(e)
        
#delete stuff method
def delete(table_name, column, variable):
    mycursor = db.cursor()
    sql = "DELETE FROM {} WHERE {} = '{}'".format(table_name, column, variable)
    mycursor.execute(sql)
    db.commit()
    
#update stuff method
def update(table_name, column, variable, column2, variable2):
    mycursor = db.cursor()
    sql = "UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(table_name, column, variable, column2, variable2)
    mycursor.execute(sql)
    db.commit()
    print("update")

#Looks through users for logging in (Select statements)
def read_users(username, password):
    mycursor = db.cursor()
    sql = "SELECT * FROM users where username = '{}' and password = '{}'".format(username, password)
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result is None:
        return False
    else:
        return True


#gets users
def get_user(username):
    mycursor = db.cursor()
    sql_user_select = "SELECT * FROM users where username = '{}'".format(username)  
    mycursor.execute(sql_user_select)  
    return mycursor.fetchone()


#to be made into an admin method
def csv_insert(file_name):
    theList = []
    with open(file_name) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader)
        for row in reader:
            mycursor = db.cursor()
            sql_user_insert = """INSERT INTO users (name, username, password, role) VALUES('{}','{}','{}', '{}')""".format(row[0],row[1],row[2],row[3])
            mycursor.execute(sql_user_insert)
            db.commit()
                #getting user
            result = get_user(row[1])
                #creating bank object
            bank_account = bank(result[0], 0)
            sql_bank = """INSERT INTO bank_accounts (balance, user_ID) VALUES('{}','{}')""".format(bank_account.balance, bank_account.user_ID)
            mycursor.execute(sql_bank)   
            db.commit()
            #insert into address
                #creating address object
            user_address = address(result[0], None, None, None, None)
            sql_user_address_insert = """INSERT INTO address (address_line, city, country, zipcode, user_ID) VALUES('{}','{}','{}','{}','{}')""".format(user_address.address_line, user_address.city, user_address.country, user_address.zipcode, user_address.user_ID)
            mycursor.execute(sql_user_address_insert)
            db.commit()
            theList.append("successfully inserted")
    newList = Counter(theList)
    for k,v in newList.items():
        print("You have {} {} accounts".format(k, v))
            
    
#Main code execution
while True:
    print("---------------------------------")
    print("- Welcome to the FCU terminal -")
    print("---------------------------------")
    action = input("What would you like to do? 0 => Exit, 1 => Create a new User, 2 => Login: ")
    if action == "0":
        quit()
    elif action == "1":
        print()
        print("--------------------------------------------------------------------")
        print("-Create your account by putting your name, username, and password-")
        print("--------------------------------------------------------------------")
        name = input("Name: ")
        username = input("Username: ")
        password = input("password: ")
        newUser = user(name, username, password, "user")
        insert_user(newUser)
    elif action == "2":
        print()
        print("--------------------------")
        print("-Put in your credentials-")
        print("--------------------------")
        username = input("username: ")
        password = input("password: ")
        if read_users(username, password) == True:
            #The User actions
            current_user = get_user(username)
            if current_user[4] == "user":
                while True:
                    print("-------------")
                    print("-Welcome {}-".format(username)) 
                    print("-------------")
                    action = input("-What would you like to do? 0 => logout, 1 => Deposit money, 2 => Withdraw money, 3 => Update address, 4 => Delete account: ")
                    if action == "0":
                        print()
                        break
                    elif action == "1":
                        mycursor = db.cursor()
                        #getting user
                        result = get_user(username)
                        #getting bank_account
                        sql_bank_select = "SELECT * FROM bank_accounts where user_ID = '{}'".format(result[0])  
                        mycursor.execute(sql_bank_select)  
                        result_bank = mycursor.fetchone()
                        #update bank
                        print("You have {}".format(result_bank[1]))
                        deposit = int(input("How much do you want to deposit?: "))
                        update("bank_accounts", "balance", (deposit+result_bank[1]), "user_id", result_bank[2])
                        
                    elif action == "2":
                        mycursor = db.cursor()
                        #getting use
                        result = get_user(username)
                        #getting bank_account
                        sql_bank_select = "SELECT * FROM bank_accounts where user_ID = '{}'".format(result[0])  
                        mycursor.execute(sql_bank_select)  
                        result_bank = mycursor.fetchone()
                        #update bank
                        print("You have {}".format(result_bank[1]))
                        withdraw = int(input("How much do you want to withdraw?: "))
                        if result_bank[1]-withdraw < 0:
                            print("you do not have enough!")
                        else:
                            update("bank_accounts", "balance", (result_bank[1]-withdraw), "user_id", result_bank[2])
                    elif action == "3":
                        mycursor = db.cursor()
                        #getting user
                        result = get_user(username)
                        #getting address
                        sql_address_select = "SELECT * FROM address where user_ID = '{}'".format(result[0])  
                        mycursor.execute(sql_address_select)  
                        result_address = mycursor.fetchone()
                        print("current address {}".format(result_address))
                        #address_line, city, country, zipcode user input
                        address_line = input("address_line: ")
                        city = input("city: ")
                        country = input("country: ")
                        zipcode = input("zipcode: ")
                        update("address", "address_line", address_line, "user_id", result[0])
                        update("address", "city",city, "user_id", result[0])
                        update("address", "country", country, "user_id", result[0])
                        update("address", "zipcode", zipcode, "user_id", result[0])
                    elif action == "4":
                        mycursor = db.cursor()
                        #getting user
                        result = get_user(username)
                        delete("address", "user_ID", result[0])
                        delete("bank_accounts", "user_ID", result[0])
                        delete("users", "user_ID", result[0])
                        print("account deleted")
                        break
                    #end of user functionality
            elif current_user[4] == "admin":
                #admin stuff
                while True:
                    print()
                    print("---------------")
                    print("-Welcome admin-")
                    print("---------------")
                    action = input("What would you like to do? 0 => logout, 1=>Insert users throught CSV: ")
                    if action == "0":
                        print()
                        break
                    elif action =="1":
                        file_name = input("What is the name of the csv file (ex. file.csv): ")
                        csv_insert(file_name)
        elif read_users(username, password) == False:
            print("No user exists")
    

