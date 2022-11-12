from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/contactform')
def contactform():
    return render_template('contactform.html')


@app.route('/logged')  # mudar isto futuramente
def logged():
    return render_template('logged.html')


@app.route('/create-acc')
def createacc():
    return render_template('createacc.html')

@app.route('/appointment')
def appointment():
    return render_template('user-appointment.html')

@app.route('/doctor-dashboard')
def doctor_dashboard():
    return render_template('doctor-dashboard.html')


@app.route('/doctor-dashboard/patients/')
def doctor_dashboard_patients():
    # here there will be a cursor.execute( "SELECT * FROM patients WHERE doctor_id = {id_of_authenticated_doctor}")
    # which will return an iterator
    """
    params_dict = {"patients": []}
    for result in iterator:
        params_dict["patients"].append({"name": result.name, "...": ..., ...})

    params_dict["total_patients"] = len(params_dict["patients"]

    """

    filtering = request.args.get('filter')
    params_dict = {}
    if filtering is None or filtering == "":
        params_dict = {"patients": [{"name": "Jeff", "niss": 12345, "id": {"_id": 1}, "last_appointment": "17/4/2019"},
                                    {"name": "Tom", "niss": 12345, "id": {"_id": 2}, "last_appointment": "20/07/2021"}],
                       "total_patients": 2}

    return render_template('doctor-dashboard-patients.html', params=params_dict)


@app.route('/doctor-dashboard/patients/<_id>')
def doctor_dashboard_patient_info(_id):
    _id = int(_id)
    if _id == 1:
        params_dict = {"patient": "Jeff", "niss": 12345, "description": "He's a very nice person.",
                       "illnesses": ["Cold"]}
    elif _id == 2:
        params_dict = {"patient": "Tom", "niss": 12345, "description": "He's a very cool person.",
                       "illnesses": ["Muscle Soreness", "Covid"]}
    else:
        params_dict = None
    return render_template('doctor-dashboard-patient-info.html', params=params_dict)


@app.route('/doctor-dashboard/appointments')
def doctor_dashboard_appointments():
    # here there will be a cursor.execute( "SELECT * FROM appointments WHERE doctor_id = {id_of_authenticated_doctor}")
    # which will return an iterator
    """
    params_dict = {"appointments": []}
    for result in iterator:
        params_dict["appointments"].append({"date": result.date, "...": ..., ...})

    params_dict["total_appointments"] = len(params_dict["appointments"]

    """

    filtering = request.args.get('filter')
    params_dict = {}
    if filtering is None or filtering == "":
        params_dict = {"appointments": [{"date": "10/11/2022", "hour": "11h", "id": {"_id": 1},
                                         "specialty": "Pediatrics", "patient": "Jeff"},
                                        {"date": "6/12/2022", "hour": "12h", "id": {"_id": 2},
                                         "specialty": "Orthopedics", "patient": "Tom"}],
                       "total_appointments": 2}

    return render_template('doctor-dashboard-appointments.html', params=params_dict)


@app.route('/doctor-dashboard/appointments/<_id>')
def doctor_dashboard_appointment_info(_id):
    _id = int(_id)
    if _id == 1:
        params_dict = {"date": "10/11/2022", "hour": "11h", "specialty": "Pediatrics",
                       "patient": "Jeff", "doctor": "Hernesto"}
    elif _id == 2:
        params_dict = {"date": "6/12/2022", "hour": "12h", "specialty": "Orthopedics",
                       "patient": "Tom", "doctor": "Hernesto"}
    else:
        params_dict = None
    return render_template('doctor-dashboard-appointment-info.html', params=params_dict)


@app.route('/doctor-dashboard/prescriptions')
def doctor_dashboard_prescriptions():

    filtering = request.args.get('filter')
    params_dict = {}
    if filtering is None or filtering == "":
        params_dict = {"prescriptions": [{"date": "10/11/2022", "id": {"_id": 1}, "patient": "Jeff"},
                                         {"date": "20/1/2021", "id": {"_id": 2}, "patient": "Tom"}],
                       "total_prescriptions": 2}

    return render_template('doctor-dashboard-prescription.html', params=params_dict)


@app.route('/doctor-dashboard/prescriptions/<_id>')
def doctor_dashboard_prescription_info(_id):
    _id = int(_id)
    if _id == 1:
        params_dict = {"date": "10/11/2022", "name": "Bruffen", "id": 1,
                       "patient": "Jeff", "motive": "He has pain in his body.",
                       "pharmaceuticals": ["Bruffen", "Paracetamol"]}
    elif _id == 2:
        params_dict = {"date": "6/12/2022", "name": "Anti-depressive", "id": 2,
                       "patient": "Tom", "Motive": "Because yes",
                       "pharmaceuticals": ["Anti-depressives", "Heroine"]}
    else:
        params_dict = None
    return render_template('doctor-dashboard-prescription-info.html', params=params_dict)


if __name__ == '__main__':
    app.run(use_reloader=True)
