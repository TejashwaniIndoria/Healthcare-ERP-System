from database.db_connection import get_connection



def get_all_doctors():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Doctors")

    doctors = cursor.fetchall()

    connection.close()

    return doctors




def add_doctor(name, specialization, phone, experience):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO Doctors
        (name, specialization, phone, experience)
        VALUES (?, ?, ?, ?)
        """,
        (
            name,
            specialization,
            phone,
            experience
        )
    )

    connection.commit()

    connection.close()

    return True




def update_doctor(doctor_id, name, specialization, phone, experience):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE Doctors
        SET name=?,
            specialization=?,
            phone=?,
            experience=?
        WHERE doctor_id=?
        """,
        (
            name,
            specialization,
            phone,
            experience,
            doctor_id
        )
    )

    connection.commit()

    connection.close()

    return True




def delete_doctor(doctor_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM Doctors WHERE doctor_id=?",
        (doctor_id,)
    )

    connection.commit()

    connection.close()

    return True




def search_doctor(keyword):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM Doctors
        WHERE name LIKE ?
        OR specialization LIKE ?
        OR phone LIKE ?
        """,
        (
            "%" + keyword + "%",
            "%" + keyword + "%",
            "%" + keyword + "%"
        )
    )

    doctors = cursor.fetchall()

    connection.close()

    return doctors