import mysql.connector as c
from flask import request

# Database connection
myconn = c.connect(host="localhost", user="root", password="1234", database="Prod_Reccomend_Sys")
mycur = myconn.cursor()

def register_acc():
    try:
        data = request.json  # Get the JSON data from the request
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
            return {"message": "Account Created Successfully!"}, 201
        else:
            return {"message": "Account already exists"}, 409  # Conflict status code
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500  # Internal server error

def login_acc():
    try:
        data = request.json  # Get the JSON data from the request
        uID = int(data.get('uID'))
        Password = data.get('Password')

        mycur.execute("SELECT * FROM User_Login WHERE uID=%s", (uID,))
        account = mycur.fetchone()

        if account is not None:
            if account[4] == Password:  # Assuming Password is the fifth column (index 4)
                return {"message": f"You Have Been Logged In: {account[1]}"}, 200  # OK status code
            else:
                return {"message": "Wrong Password"}, 401  # Unauthorized status code
        else:
            return {"message": "Account does not exist"}, 404  # Not found status code
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500  # Internal server error
