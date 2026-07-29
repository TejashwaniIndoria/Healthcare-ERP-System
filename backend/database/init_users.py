import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from database.db_connection import get_connection



connection = get_connection()

cursor = connection.cursor()



cursor.execute(
"""
INSERT INTO Users
(username,password,role)

VALUES
('admin','admin123','Admin'),

('doctor','doctor123','Doctor'),

('reception','reception123','Receptionist')
"""
)



connection.commit()

connection.close()


print("Users created successfully")