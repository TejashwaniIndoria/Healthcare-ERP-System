from database.db_connection import get_connection



def get_all_appointments():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT 
        Appointments.appointment_id,
        Patients.name AS patient_name,
        Doctors.name AS doctor_name,
        appointment_date,
        appointment_time,
        status

        FROM Appointments

        JOIN Patients
        ON Appointments.patient_id = Patients.patient_id

        JOIN Doctors
        ON Appointments.doctor_id = Doctors.doctor_id
        """
    )


    appointments = cursor.fetchall()

    connection.close()

    return appointments




def add_appointment(patient_id, doctor_id, date, time, status):

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        """
        INSERT INTO Appointments
        (
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time,
        status
        )

        VALUES (?, ?, ?, ?, ?)

        """,

        (
            patient_id,
            doctor_id,
            date,
            time,
            status
        )

    )


    connection.commit()

    connection.close()


    return True