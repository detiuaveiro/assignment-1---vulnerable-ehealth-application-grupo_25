from flask import Flask, redirect, url_for, render_template, request, session, flash
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
  host="localhost",
  user="daniel",
  password="8495",
  database="eHealthCorp"
)

cur = db.cursor()



@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        pw = request.form["pw"]
        session["email"] = email

        users = cur.execute("SELECT Email, Password FROM Utilizador WHERE Email=%s", email).fetchall()

        if len(users) == 0:
            flash("This account doesn't exist!")
        else:
            if:
                pass


        if found_user:
            session["email"] = found_user.email
        else:
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

        flash("Login succesful", "info")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!", "info")
            redirect(url_for("user"))
        return render_template("login.html")


if __name__ == '__main__':
    app.run()
