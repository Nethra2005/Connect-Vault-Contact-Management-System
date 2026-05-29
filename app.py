from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "connectvaultsecret"

client = MongoClient("mongodb://localhost:27017/")
db = client["connect_vault"]
users = db["users"]
contacts = db["contacts"]

@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    q = request.args.get("q","")
    data = list(contacts.find({"name":{"$regex":q,"$options":"i"}})) if q else list(contacts.find())
    return render_template("index.html", contacts=data)

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method=="POST":
        users.insert_one({"username":request.form["username"],"password":generate_password_hash(request.form["password"])})
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        user = users.find_one({"username":request.form["username"]})
        if user and check_password_hash(user["password"], request.form["password"]):
            session["user"]=user["username"]
            return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/add", methods=["GET","POST"])
def add():
    if request.method=="POST":
        contacts.insert_one(dict(name=request.form["name"],phone=request.form["phone"],email=request.form["email"],address=request.form["address"]))
        return redirect("/")
    return render_template("add_contact.html")

@app.route("/edit/<id>", methods=["GET","POST"])
def edit(id):
    c = contacts.find_one({"_id":ObjectId(id)})
    if request.method=="POST":
        contacts.update_one({"_id":ObjectId(id)},{"$set":{
            "name":request.form["name"],
            "phone":request.form["phone"],
            "email":request.form["email"],
            "address":request.form["address"]
        }})
        return redirect("/")
    return render_template("edit_contact.html", c=c)

@app.route("/delete/<id>")
def delete(id):
    contacts.delete_one({"_id":ObjectId(id)})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
