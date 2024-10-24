import mysql.connector as c

# Establishing the connection
myconn = c.connect(host="localhost", user="root", password="1234", database="Bnk_Mgmt")
mycur = myconn.cursor()

# Create Accounts table
query = '''
CREATE TABLE IF NOT EXISTS Accounts (
    uid INT PRIMARY KEY,
    name VARCHAR(30),
    password INT,
    balance INT
)
'''
mycur.execute(query)

# Function to create a new account
def create_acc():
    uid = int(input("Enter Unique ID assigned: "))
    mycur.execute("SELECT * FROM Accounts WHERE uid=%s", (uid,))
    account = mycur.fetchone()
    
    if account is None:
        name = input("Enter Your Name: ")
        password = int(input("Create Password: "))
        balance = int(input("Enter Initial Balance: "))
        
        sql = "INSERT INTO Accounts (uid, name, password, balance) VALUES (%s, %s, %s, %s)"
        val = (uid, name, password, balance)
        mycur.execute(sql, val)
        myconn.commit()
        print("Account Created Successfully!!")
    else:
        print("Account already Exists")

def disp_acc():
    uid = int(input("Enter Unique ID Assigned: "))
    mycur.execute("SELECT * FROM Accounts WHERE uid=%s", (uid,))
    account = mycur.fetchone()
    
    if account is not None:
        password = int(input("Enter Your Password: "))
        if account[2] == password:
            print(f"Your Current Balance is: {account[3]}")
        else:
            print("Wrong Password")
    else:
        print("Account does not exist")

        print("Enter a valid choice (1-5)")
