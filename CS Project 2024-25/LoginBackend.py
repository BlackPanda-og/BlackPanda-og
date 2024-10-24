import mysql.connector as c
myconn = c.connect(host="localhost", user="root", password="1234", database="Userlogin_sys")
mycur = myconn.cursor()

# Function to create a new account
def Register_acc():
    uID = int(input("Enter Unique ID assigned: "))
    mycur.execute("SELECT * FROM Accounts WHERE uID=%s", (uID,))
    account = mycur.fetchone()
    
    if account is None:
        name = input("Enter Your Name: ")
        password = int(input("Create Password: "))
        email = int(input("Enter Your Email ID: "))
        
        sql = "INSERT INTO Accounts (uID, name, password, email) VALUES (%s, %s, %s, %s)"
        val = (uID, name, password, email)
        mycur.execute(sql, val)
        myconn.commit()
        print("Account Created Successfully!!")
    else:
        print("Account already Exists")

def Login_acc():
    uid = int(input("Enter Unique ID Assigned: "))
    mycur.execute("SELECT * FROM Accounts WHERE uid=%s", (uid,))
    account = mycur.fetchone()
    
    if account is not None:
        password = int(input("Enter Your Password: "))
        if account[2] == password:
            print(f"You Have Been Registered: {account[1]}")
        else:
            print("Wrong Password")
    else:
        print("Account does not exist")
