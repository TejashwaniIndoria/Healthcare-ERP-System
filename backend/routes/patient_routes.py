from flask import Blueprint, jsonify, request

from models.patient import (
    get_all_patients,
    add_patient,
    delete_patient,
    update_patient,
    search_patient
)


patient_bp = Blueprint(
    "patient",
    __name__
)


@patient_bp.route("/patients", methods=["GET"])
def patients():

    data = get_all_patients()

    patients = []

    for patient in data:
        patients.append(dict(patient))

    return jsonify(patients)



@patient_bp.route("/patients", methods=["POST"])
def create_patient():

    data = request.json

    add_patient(
        data["name"],
        data["age"],
        data["gender"],
        data["phone"],
        data["disease"]
    )

    return jsonify({
        "message": "Patient added successfully"
    })

@patient_bp.route("/patients/<int:patient_id>", methods=["DELETE"])
def remove_patient(patient_id):

    delete_patient(patient_id)

    return jsonify({
        "message": "Patient deleted successfully"
    })
@patient_bp.route("/patients/<int:patient_id>", methods=["PUT"])
def edit_patient(patient_id):

    data = request.json

    update_patient(
        patient_id,
        data["name"],
        data["age"],
        data["gender"],
        data["phone"],
        data["disease"]
    )

    return jsonify({
        "message": "Patient updated successfully"
    })
@patient_bp.route("/patients/search/<keyword>", methods=["GET"])
def search(keyword):

    data = search_patient(keyword)

    patients = []

    for patient in data:
        patients.append(dict(patient))

    return jsonify(patients)