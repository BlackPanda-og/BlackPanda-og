import mysql.connector as c
myconn = c.connect(host="localhost", user="root", password="1234", database="Prod_Reccomend_Sys")
mycur = myconn.cursor()

# Function to create a new account
def Register_acc():
    uID = int(input("Enter Unique ID assigned: "))
    mycur.execute("SELECT * FROM User_Login WHERE uID=%s", (uID,))
    account = mycur.fetchone()
    
    if account is None:
        Name = input("Enter Your Name: ")
        Password = int(input("Create Password: "))
        Email_ID = int(input("Enter Your Email ID: "))
        Contact_No= int(input("Enter Your Contact No: "))
        sql = "INSERT INTO UserLogin(uID, Name, Password, Email_ID,Contact_No) VALUES (%s, %s, %s, %s,%s)"
        val = (uID, Name, Password, Email_ID,Contact_No)
        mycur.execute(sql, val)
        myconn.commit()
        print("Account Created Successfully!!")
    else:
        print("Account already Exists")

def Login_acc():
    uid = int(input("Enter Unique ID Assigned: "))
    mycur.execute("SELECT * FROM User_Login WHERE uID=%s", (uID,))
    account = mycur.fetchone()
    
    if account is not None:
        password = int(input("Enter Your Password: "))
        if account[2] == password:
            print(f"You Have Been Registered: {User_login[1]}")
        else:
            print("Wrong Password")
    else:
        print("Account does not exist")
