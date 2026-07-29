from flask import Blueprint, jsonify, request

from models.doctor import (
    get_all_doctors,
    add_doctor,
    update_doctor,
    delete_doctor,
    search_doctor
)


doctor_bp = Blueprint(
    "doctor",
    __name__
)



@doctor_bp.route("/doctors", methods=["GET"])
def doctors():

    data = get_all_doctors()

    doctors = []

    for doctor in data:
        doctors.append(dict(doctor))

    return jsonify(doctors)




@doctor_bp.route("/doctors", methods=["POST"])
def create_doctor():

    data = request.json

    add_doctor(
        data["name"],
        data["specialization"],
        data["phone"],
        data["experience"]
    )


    return jsonify({
        "message": "Doctor added successfully"
    })
@doctor_bp.route("/doctors/<int:doctor_id>", methods=["PUT"])
def edit_doctor(doctor_id):

    data = request.json

    update_doctor(
        doctor_id,
        data["name"],
        data["specialization"],
        data["phone"],
        data["experience"]
    )

    return jsonify({
        "message": "Doctor updated successfully"
    })
@doctor_bp.route("/doctors/<int:doctor_id>", methods=["DELETE"])
def remove_doctor(doctor_id):

    delete_doctor(doctor_id)

    return jsonify({
        "message": "Doctor deleted successfully"
    })
@doctor_bp.route("/doctors/search/<keyword>", methods=["GET"])
def search(keyword):

    data = search_doctor(keyword)

    doctors = []

    for doctor in data:
        doctors.append(dict(doctor))

    return jsonify(doctors)