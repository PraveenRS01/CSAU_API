from flask import jsonify, request
from csau import app, db
from csau.models import User, user_schema, users_schema
from csau.validators import validate_user


@app.route("/")
def home():
    return jsonify({"msg": "hellooo"})


@app.route("/user", methods=["POST"])
def add_user():
    try:
        req = request.get_json()

        condition, msg = validate_user(req)

        if not condition:
            return jsonify(msg)

        username = req["username"]
        reg_no = req["reg_no"]
        department = req["department"]
        tag = req["tag"]
        domain = req["domain"]
        mobile_no = req["mobile_no"]
        email = req["email"]

        new_user = User(username, reg_no, department, tag, domain, mobile_no, email)

        db.session.add(new_user)
        db.session.commit()

        return user_schema.jsonify(new_user)

    except:
        return jsonify({"message": "Server error"})


@app.route("/user", methods=["GET"])
def get_users():
    try:
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return jsonify(result)
    except:
        return jsonify({"message": "Server error"})


@app.route("/user/<int:id>", methods=["GET"])
def get_user(id):
    try:
        user = User.query.get(id)
        return user_schema.jsonify(user)
    except:
        return jsonify({"message": "Server error"})


@app.route("/user/<int:id>", methods=["PUT"])
def update_user(id):
    try:
        req = request.get_json()

        user = User.query.get(id)

        username = req["username"]
        reg_no = req["reg_no"]
        department = req["department"]
        tag = req["tag"]
        domain = req["domain"]
        mobile_no = req["mobile_no"]
        email = req["email"]

        user.username = username
        user.reg_no = reg_no
        user.department = department
        user.tag = tag
        user.domain = domain
        user.mobile_no = mobile_no
        user.email = email

        db.session.commit()

        return user_schema.jsonify(user)
    except:
        return jsonify({"message": "Server error"})


@app.route("/user/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()

        return user_schema.jsonify(user)
    except:
        return jsonify({"message": "Server error"})
