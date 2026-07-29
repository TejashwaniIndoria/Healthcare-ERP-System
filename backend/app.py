from flask import Flask
from flask_cors import CORS


from routes.patient_routes import patient_bp
from routes.doctor_routes import doctor_bp
from routes.appointment_routes import appointment_bp
from routes.dashboard_routes import dashboard_bp
from routes.auth_routes import auth_bp



app = Flask(__name__)


# Allow frontend (localhost:5500) to access backend (localhost:5000)

CORS(
    app,
    resources={
        r"/*": {
            "origins": "*"
        }
    }
)



# Register all modules

app.register_blueprint(patient_bp)

app.register_blueprint(doctor_bp)

app.register_blueprint(appointment_bp)

app.register_blueprint(dashboard_bp)

app.register_blueprint(auth_bp)




@app.route("/")
def home():

    return "Healthcare ERP Backend Running"





if __name__ == "__main__":

    app.run(
        debug=True
    )