from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector as c

app = Flask(__name__)
CORS(app)

# Database connection
myconn = c.connect(host="localhost", user="root", password="1234", database="Prod_Reccomend_Sys")
mycur = myconn.cursor()

@app.route('/register', methods=['POST'])
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
            return jsonify({"message": "Account Created Successfully!"}), 201
        else:
            return jsonify({"message": "Account already exists"}), 400
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

@app.route('/login', methods=['POST'])
def login_acc():
    try:
        data = request.json
        uID = int(data.get('uID'))
        Password = data.get('Password')

        mycur.execute("SELECT * FROM User_Login WHERE uID=%s", (uID,))
        account = mycur.fetchone()

        if account is not None:
            if account[2] == Password:  # Assuming Password is the third column
                return jsonify({"message": f"You Have Been Logged In: {account[1]}"}), 200
            else:
                return jsonify({"message": "Wrong Password"}), 401
        else:
            return jsonify({"message": "Account does not exist"}), 404
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
