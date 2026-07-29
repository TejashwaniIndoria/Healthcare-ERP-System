// ================= API URLs =================

const PATIENT_API = "http://127.0.0.1:5000/patients";
const DOCTOR_API = "http://127.0.0.1:5000/doctors";
const APPOINTMENT_API = "http://127.0.0.1:5000/appointments";
const DASHBOARD_API = "http://127.0.0.1:5000/dashboard";
const LOGIN_API = "http://127.0.0.1:5000/login";



// ================= VARIABLES =================

let role = localStorage.getItem("role");
let username = localStorage.getItem("username");

let editPatientId = null;
let editDoctorId = null;



// ================= PAGE LOAD =================

window.onload = function () {

    if (role && username) {

        showERP();

    } else {

        document.getElementById("loginSection").style.display = "block";
        document.getElementById("erpSection").style.display = "none";

    }

};



// ================= LOGIN =================

function login() {

    const user = {

        username: document.getElementById("username").value.trim(),

        password: document.getElementById("password").value.trim()

    };

    fetch(LOGIN_API, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(user)

    })

    .then(response => response.json())

    .then(data => {

        if (data.message === "Login successful") {

            localStorage.setItem("role", data.role);
            localStorage.setItem("username", data.username);

            role = data.role;
            username = data.username;

            showERP();

        }

        else {

            alert("Invalid Username or Password");

        }

    })

    .catch(error => {

        console.log(error);

        alert("Server Error");

    });

}



// ================= SHOW ERP =================

function showERP() {

    document.getElementById("loginSection").style.display = "none";

    document.getElementById("erpSection").style.display = "block";

    document.getElementById("userRole").innerText =
        username + " (" + role + ")";

    loadDashboard();

    loadPatients();

    loadDoctors();

    loadAppointmentPatients();

    loadAppointmentDoctors();

    loadAppointments();

    applyRolePermissions();

}



// ================= LOGOUT =================

function logout() {

    localStorage.clear();

    role = null;
    username = null;

    document.getElementById("erpSection").style.display = "none";

    document.getElementById("loginSection").style.display = "block";

}



// ================= ROLE =================

function applyRolePermissions() {

    document.getElementById("patientSection").style.display = "block";

    document.getElementById("doctorSection").style.display = "block";

    if (role === "Doctor") {

        document.getElementById("patientSection").style.display = "none";

        document.getElementById("doctorSection").style.display = "none";

    }

    if (role === "Receptionist") {

        document.getElementById("doctorSection").style.display = "none";

    }

}
// ================= DASHBOARD =================

function loadDashboard() {

    fetch(DASHBOARD_API)

    .then(response => response.json())

    .then(data => {

        document.getElementById("totalPatients").innerText =
            data.total_patients;

        document.getElementById("totalDoctors").innerText =
            data.total_doctors;

        document.getElementById("todayAppointments").innerText =
            data.today_appointments;

        document.getElementById("commonDisease").innerText =
            data.common_disease;

    });

}



// ================= PATIENT MODULE =================

function loadPatients() {

    fetch(PATIENT_API)

    .then(response => response.json())

    .then(data => {

        displayPatients(data);

    });

}



function displayPatients(data) {

    let table =
        document.querySelector("#patientTable tbody");

    table.innerHTML = "";

    data.forEach(patient => {

        table.innerHTML += `

<tr>

<td>${patient.patient_id}</td>

<td>${patient.name}</td>

<td>${patient.age}</td>

<td>${patient.gender}</td>

<td>${patient.phone}</td>

<td>${patient.disease}</td>

<td>

<button onclick="editPatient(${patient.patient_id})">

Edit

</button>

<button onclick="deletePatient(${patient.patient_id})">

Delete

</button>

</td>

</tr>

`;

    });

}



function addPatient() {

    let patient = {

        name:
            document.getElementById("name").value,

        age:
            parseInt(document.getElementById("age").value),

        gender:
            document.getElementById("gender").value,

        phone:
            document.getElementById("phone").value,

        disease:
            document.getElementById("disease").value

    };



    let method =
        editPatientId ? "PUT" : "POST";



    let url =
        editPatientId ?
        PATIENT_API + "/" + editPatientId :
        PATIENT_API;



    fetch(url, {

        method: method,

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(patient)

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        editPatientId = null;

        loadPatients();

        loadDashboard();

    });

}
// ================= PATIENT CONTINUED =================

function deletePatient(id) {

    fetch(PATIENT_API + "/" + id, {

        method: "DELETE"

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        loadPatients();

        loadDashboard();

    });

}



function editPatient(id) {

    fetch(PATIENT_API)

    .then(response => response.json())

    .then(data => {

        let patient = data.find(p => p.patient_id === id);

        if (!patient) return;

        document.getElementById("name").value =
            patient.name;

        document.getElementById("age").value =
            patient.age;

        document.getElementById("gender").value =
            patient.gender;

        document.getElementById("phone").value =
            patient.phone;

        document.getElementById("disease").value =
            patient.disease;

        editPatientId = id;

    });

}



function searchPatients() {

    let keyword =
        document.getElementById("patientSearch").value;

    if (keyword.trim() === "") {

        loadPatients();

        return;

    }

    fetch(PATIENT_API + "/search/" + keyword)

    .then(response => response.json())

    .then(data => {

        displayPatients(data);

    });

}



// ================= DOCTOR MODULE =================

function loadDoctors() {

    fetch(DOCTOR_API)

    .then(response => response.json())

    .then(data => {

        displayDoctors(data);

    });

}



function displayDoctors(data) {

    let table =
        document.querySelector("#doctorTable tbody");

    table.innerHTML = "";

    data.forEach(doctor => {

        table.innerHTML += `

<tr>

<td>${doctor.doctor_id}</td>

<td>${doctor.name}</td>

<td>${doctor.specialization}</td>

<td>${doctor.phone}</td>

<td>${doctor.experience}</td>

<td>

<button onclick="editDoctor(${doctor.doctor_id})">

Edit

</button>

<button onclick="deleteDoctor(${doctor.doctor_id})">

Delete

</button>

</td>

</tr>

`;

    });

}



function addDoctor() {

    let doctor = {

        name:
            document.getElementById("doctorName").value,

        specialization:
            document.getElementById("specialization").value,

        phone:
            document.getElementById("doctorPhone").value,

        experience:
            parseInt(document.getElementById("experience").value)

    };



    let method =
        editDoctorId ? "PUT" : "POST";



    let url =
        editDoctorId ?
        DOCTOR_API + "/" + editDoctorId :
        DOCTOR_API;



    fetch(url, {

        method: method,

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(doctor)

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        editDoctorId = null;

        loadDoctors();

        loadDashboard();

    });

}
// ================= DOCTOR CONTINUED =================

function deleteDoctor(id) {

    fetch(DOCTOR_API + "/" + id, {

        method: "DELETE"

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        loadDoctors();

        loadDashboard();

    });

}



function editDoctor(id) {

    fetch(DOCTOR_API)

    .then(response => response.json())

    .then(data => {

        let doctor = data.find(d => d.doctor_id === id);

        if (!doctor) return;

        document.getElementById("doctorName").value =
            doctor.name;

        document.getElementById("specialization").value =
            doctor.specialization;

        document.getElementById("doctorPhone").value =
            doctor.phone;

        document.getElementById("experience").value =
            doctor.experience;

        editDoctorId = id;

    });

}



function searchDoctors() {

    let keyword =
        document.getElementById("doctorSearch").value;

    if (keyword.trim() === "") {

        loadDoctors();

        return;

    }

    fetch(DOCTOR_API + "/search/" + keyword)

    .then(response => response.json())

    .then(data => {

        displayDoctors(data);

    });

}



// ================= APPOINTMENT MODULE =================

function loadAppointmentPatients() {

    fetch(PATIENT_API)

    .then(response => response.json())

    .then(data => {

        let dropdown =
            document.getElementById("appointmentPatient");

        dropdown.innerHTML =
            "<option value=''>Select Patient</option>";

        data.forEach(patient => {

            dropdown.innerHTML += `
                <option value="${patient.patient_id}">
                    ${patient.name}
                </option>
            `;

        });

    });

}



function loadAppointmentDoctors() {

    fetch(DOCTOR_API)

    .then(response => response.json())

    .then(data => {

        let dropdown =
            document.getElementById("appointmentDoctor");

        dropdown.innerHTML =
            "<option value=''>Select Doctor</option>";

        data.forEach(doctor => {

            dropdown.innerHTML += `
                <option value="${doctor.doctor_id}">
                    ${doctor.name}
                </option>
            `;

        });

    });

}



function addAppointment() {

    let appointment = {

        patient_id:
            document.getElementById("appointmentPatient").value,

        doctor_id:
            document.getElementById("appointmentDoctor").value,

        appointment_date:
            document.getElementById("appointmentDate").value,

        appointment_time:
            document.getElementById("appointmentTime").value,

        status:
            document.getElementById("appointmentStatus").value

    };

    fetch(APPOINTMENT_API, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(appointment)

    })

    .then(response => response.json())

    .then(data => {

        alert(data.message);

        loadAppointments();

        loadDashboard();

    });

}
// ================= LOAD APPOINTMENTS =================

function loadAppointments() {

    fetch(APPOINTMENT_API)

    .then(response => response.json())

    .then(data => {

        let table =
            document.querySelector("#appointmentTable tbody");

        table.innerHTML = "";

        data.forEach(app => {

            table.innerHTML += `

<tr>

<td>${app.appointment_id}</td>

<td>${app.patient_name}</td>

<td>${app.doctor_name}</td>

<td>${app.appointment_date}</td>

<td>${app.appointment_time}</td>

<td>${app.status}</td>

</tr>

`;

        });

    });

}