CREATE TABLE IF NOT EXISTS Patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    phone TEXT,
    disease TEXT
);


CREATE TABLE IF NOT EXISTS Doctors (

    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    specialization TEXT NOT NULL,

    phone TEXT,

    experience INTEGER

);
CREATE TABLE IF NOT EXISTS Appointments (

    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,

    patient_id INTEGER,

    doctor_id INTEGER,

    appointment_date TEXT,

    appointment_time TEXT,

    status TEXT,

    FOREIGN KEY(patient_id) REFERENCES Patients(patient_id),

    FOREIGN KEY(doctor_id) REFERENCES Doctors(doctor_id)

);
CREATE TABLE IF NOT EXISTS Users (

    user_id INTEGER PRIMARY KEY AUTOINCREMENT,

    username TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    role TEXT NOT NULL

);