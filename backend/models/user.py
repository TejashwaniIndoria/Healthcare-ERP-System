from database.db_connection import get_connection



def login_user(username, password):


    connection = get_connection()

    cursor = connection.cursor()



    cursor.execute(
        """
        SELECT *
        FROM Users
        WHERE username=?
        AND password=?
        """,
        (
            username,
            password
        )
    )


    user = cursor.fetchone()


    connection.close()


    return user