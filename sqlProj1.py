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

# Function to deposit money
def deps_amt():
    uid = int(input("Enter Unique ID Assigned: "))
    mycur.execute("SELECT * FROM Accounts WHERE uid=%s", (uid,))
    account = mycur.fetchone()
    
    if account is not None:
        password = int(input("Enter Your Password: "))
        if account[2] == password:
            dep_amt = int(input("Enter Amount to Deposit: "))
            new_balance = account[3] + dep_amt
            mycur.execute("UPDATE Accounts SET balance=%s WHERE uid=%s", (new_balance, uid))
            myconn.commit()
            print("Money Successfully Deposited")
        else:
            print("Wrong Password")
    else:
        print("Account does not exist")

# Function to withdraw money
def wdraw_amt():
    uid = int(input("Enter Unique ID Assigned: "))
    mycur.execute("SELECT * FROM Accounts WHERE uid=%s", (uid,))
    account = mycur.fetchone()
    
    if account is not None:
        password = int(input("Enter Your Password: "))
        if account[2] == password:
            wdraw_amt = int(input("Enter Amount to Withdraw: "))
            if wdraw_amt > account[3]:
                print("Insufficient Funds!!")
            else:
                new_balance = account[3] - wdraw_amt
                mycur.execute("UPDATE Accounts SET balance=%s WHERE uid=%s", (new_balance, uid))
                myconn.commit()
                print("Money Successfully Withdrawn")
        else:
            print("Wrong Password")
    else:
        print("Account does not exist")

# Function to display account balance
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

# Main program
ch = 1
while ch != 5:
    print("1) Create Bank Account\n2) Deposit Money\n3) Withdraw Money\n4) Display Balance\n5) Exit")
    ch = int(input("Enter Choice: "))
    
    if ch == 1:
        create_acc()
    elif ch == 2:
        deps_amt()
    elif ch == 3:
        wdraw_amt()
    elif ch == 4:
        disp_acc()
    elif ch == 5:
        print("Thank you for using our services")
    else:
        print("Enter a valid choice (1-5)")
