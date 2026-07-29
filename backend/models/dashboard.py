from database.db_connection import get_connection



def get_dashboard_data():

    connection = get_connection()

    cursor = connection.cursor()


    cursor.execute(
        "SELECT COUNT(*) FROM Patients"
    )

    total_patients = cursor.fetchone()[0]



    cursor.execute(
        "SELECT COUNT(*) FROM Doctors"
    )

    total_doctors = cursor.fetchone()[0]



    cursor.execute(
        """
        SELECT COUNT(*)
        FROM Appointments
        WHERE appointment_date = DATE('now')
        """
    )

    today_appointments = cursor.fetchone()[0]



    cursor.execute(
        """
        SELECT disease, COUNT(*) as count
        FROM Patients
        GROUP BY disease
        ORDER BY count DESC
        LIMIT 1
        """
    )

    result = cursor.fetchone()


    common_disease = result["disease"] if result else "None"



    connection.close()


    return {

        "total_patients": total_patients,

        "total_doctors": total_doctors,

        "today_appointments": today_appointments,

        "common_disease": common_disease

    }