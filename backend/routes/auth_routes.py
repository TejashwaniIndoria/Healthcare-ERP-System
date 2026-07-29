from flask import Blueprint, request, jsonify

from models.user import login_user



auth_bp = Blueprint(
    "auth",
    __name__
)



@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.json


    user = login_user(
        data["username"],
        data["password"]
    )


    if user:


        return jsonify({

            "message": "Login successful",

            "username": user["username"],

            "role": user["role"]

        })


    return jsonify({

        "message": "Invalid username or password"

    }),401