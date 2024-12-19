import mysql.connector as c

# Database connection
myconn = c.connect(host="localhost", user="root", password="1234", database="Prod_Reccomend_Sys")
mycur = myconn.cursor()

def register_acc():
    try:
        data = request.json
        uID = int(data.get('uID'))
        Name = data.get('Name')
        Password = data.get('Password')
        Email_ID = data.get('Email_ID')
        Contact_No = data.get('Contact_No')

        mycur.execute("SELECT * FROM User_Login WHERE uID=%s", (uID,))
        account = mycur.fetchone()

        if account is None:
            sql = "INSERT INTO User_Login (uID, Name, Password, Email_ID, Contact_No) VALUES (%s, %s, %s, %s, %s)"
            val = (uID, Name, Password, Email_ID, Contact_No)
            mycur.execute(sql, val)
            myconn.commit()
            return ({"message": "Account Created Successfully!"}), 201
        else:
            return ({"message": "Account already exists"})
    except Exception as e:
        return ({"message": f"An error occurred: {str(e)}"})

def login_acc():
    try:
        data = request.json
        uID = int(data.get('uID'))
        Password = data.get('Password')

        mycur.execute("SELECT * FROM User_Login WHERE uID=%s", (uID,))
        account = mycur.fetchone()

        if account is not None:
            if account[2] == Password:  # Assuming Password is the third column
                return ({"message": f"You Have Been Logged In: {account[1]}"}) 
            else:
                return ({"message": "Wrong Password"})
        else:
            return ({"message": "Account does not exist"})
    except Exception as e:
        return ({"message": f"An error occurred: {str(e)}"})

