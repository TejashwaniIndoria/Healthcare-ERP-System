from flask import Blueprint, jsonify, request


from models.appointment import (
    get_all_appointments,
    add_appointment
)



appointment_bp = Blueprint(
    "appointment",
    __name__
)




@appointment_bp.route("/appointments", methods=["GET"])
def appointments():


    data = get_all_appointments()


    appointments=[]


    for appointment in data:

        appointments.append(dict(appointment))


    return jsonify(appointments)





@appointment_bp.route("/appointments", methods=["POST"])
def create_appointment():


    data=request.json


    add_appointment(

        data["patient_id"],

        data["doctor_id"],

        data["date"],

        data["time"],

        data["status"]

    )


    return jsonify({

        "message":"Appointment created successfully"

    })