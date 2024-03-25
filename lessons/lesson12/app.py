from flask import Flask, request, render_template, redirect
from models import User

my_app = Flask(__name__)


# Generate list of 10 users
USERS = [
    User(1, "john_doe", "john.doe@email.com"),
    User(2, "jane_doe", "jane.doe@email.com"),
    User(3, "alice", "alice@email.com"),
    User(4, "bob", "bob@email.com"),
    User(5, "charlie", "charlie@email.com"),
    User(6, "david", "david@email.com"),
    User(7, "emma", "emma@email.com"),
    User(8, "frank", "frank@email.com"),
    User(9, "grace", "grace@email.com"),
    User(10, "hannah", "hannah@email.com"),
]


@my_app.route("/users", methods=['GET', 'POST'])
def user_list():
    if request.method == "GET":
        return render_template("userlist.html", my_data=USERS)
        # return [user.to_dict() for user in USERS]
    elif request.method == "POST":
        pk = max(USERS, key= lambda user: user.id).id +1
        username = request.form['username'] 
        email = request.form['email'] 
        user = User(pk, username, email)
        USERS.append(user)
        return redirect("/users")

@my_app.route("/users/<int:id>", methods=['GET', 'POST'])
def user_update(id):
    user = [user for user in USERS if user.id == id]
    if request.method == "GET":
        if user:
            return render_template("user_update.html", user=user[0])
        return render_template("user_update.html", err="User not found!!!")
    elif request.method == "POST":
        user[0].update(request.form['username'], request.form['email'])
        return redirect("/users")

if __name__ == '__main__':
    my_app.run(host="0.0.0.0", port=3001)