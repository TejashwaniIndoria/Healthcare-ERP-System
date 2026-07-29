from database.db_connection import get_connection


def get_all_patients():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Patients")

    patients = cursor.fetchall()

    connection.close()

    return patients


def add_patient(name, age, gender, phone, disease):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO Patients
        (name, age, gender, phone, disease)
        VALUES (?, ?, ?, ?, ?)
        """,
        (name, age, gender, phone, disease)
    )

    connection.commit()

    connection.close()

    return True


def delete_patient(patient_id):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM Patients WHERE patient_id=?",
        (patient_id,)
    )

    connection.commit()

    connection.close()

    return True
def update_patient(patient_id, name, age, gender, phone, disease):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE Patients
        SET name=?,
            age=?,
            gender=?,
            phone=?,
            disease=?
        WHERE patient_id=?
        """,
        (name, age, gender, phone, disease, patient_id)
    )

    connection.commit()

    connection.close()

    return True
def search_patient(keyword):

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM Patients
        WHERE name LIKE ?
        OR disease LIKE ?
        OR phone LIKE ?
        """,
        (
            "%" + keyword + "%",
            "%" + keyword + "%",
            "%" + keyword + "%"
        )
    )

    patients = cursor.fetchall()

    connection.close()

    return patients