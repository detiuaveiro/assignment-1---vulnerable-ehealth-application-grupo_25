from flask import Flask, render_template, request, flash, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


db = mysql.connector.connect(
    host="localhost",
    #port=3307,
    #user="root",
    #password="1904",
    #user="daniel",
    #password="8495",
    #database="eHealthCorp"
    user="bruna",
    password="12345678",
    database="sio_db"
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    params_dict = {"email": "", "password": "", "id": ""}

    if request.method == 'POST':
        params_dict["email"] = request.form['email']
        params_dict["password"] = request.form['password']

        # Buscar email e pass à base de dados
        cursor = db.cursor()

        cursor.execute("SELECT ID, Email, Password FROM Utilizador WHERE Email = %s AND Password = %s", (params_dict["email"], params_dict["password"]))
        user_data = cursor.fetchone()


        if user_data is None:
            flash("Email or password incorrect")
            return redirect(url_for('login'))
        else:
            params_dict["id"] = user_data[0]

            session['user_id'] = params_dict["id"]
            session['email'] = user_data[1]

            # Verificar se é médico ou paciente e redirecionar para a página correta
            cursor.execute("SELECT ID FROM Medico WHERE ID = %s", (params_dict["id"],))
            medico_data = cursor.fetchone()

            if medico_data is None:
                # É paciente
                return redirect(url_for('logged'))
            else:
                # É médico
                return redirect(url_for('doctor_dashboard'))
            
    return render_template('login.html')

def logout():
    if session.get('user_id') is not None:
        session.pop('user_id', None)
        session.pop('email', None)

    flash("Logged out successfully")
    return redirect(url_for('index'))


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

# doctor-dashboard
@app.route('/doctor-dashboard')
def doctor_dashboard():
    # to be completed, doctor-dashboard.html is prepared to receive params
    return render_template('doctor-dashboard.html', params={})


@app.route('/doctor-dashboard/patients/', methods=["GET", "POST"])
def doctor_dashboard_patients():
    # here there will be a cursor.execute( "SELECT * FROM patients WHERE doctor_id = {id_of_authenticated_doctor}")
    # which will return an iterator
    # TODO: Get the last appointment date of a patient (Save it in the DB? Query using table Consulta?)
    # TODO: Search bar query: Check to see if the flash message is appearing when searching for query with no results, once Sessions have been implemented
    # TODO: Replace with commented version once login of autenthicated users is setup
    """
    params_dict = {"patients": []}
    for result in iterator:
        params_dict["patients"].append({"name": result.name, "...": ..., ...})

    params_dict["total_patients"] = len(params_dict["patients"]

    """
    params_dict = {"patients": [], "total_patients": 0}

    if request.method == "GET":
        '''
        doctor_id = session["user_ID"]
        
        patients_ID = db.cursor()
        patients_ID.execute("SELECT * FROM Med_Pac WHERE ID_Med=%s", (doctor_id,))

        for ID in patients_ID:
            patient_NISS = db.cursor()
            patient_NISS.execute("SELECT Paciente.ID, Nome, Num_Utente FROM Paciente JOIN Utilizador U on U.ID = Paciente.ID WHERE ID=%s", (ID, ))
            patient = patient_NISS.fetchone()[0]

            # Adicionar info ao params_dict
            params_dict["patients"].append({"name":patient[1], "niss": patient[-1], "id": {"_id": ID}, "last_appointment": "17/4/2019"})
            params_dict["total_patients"] += 1

            patient_NISS.close()
        '''

        # For testing purposes:
        patients = db.cursor()
        patients.execute("SELECT Paciente.ID AS ID, Nome, Num_Utente FROM Paciente JOIN Utilizador U on Paciente.ID = U.ID")

        for (ID, Nome, Num_Utente) in patients:
            params_dict["patients"].append({"name": Nome, "niss": Num_Utente, "id": {"_id": ID}, "last_appointment": "17/4/2019"})
            params_dict["total_patients"] += 1


        patients.close()

    elif request.method == "POST":
        filter = "%" + request.form["filter"] + "%"

        patients = db.cursor()
        patients.execute("select Utilizador.ID, Nome, Num_Utente from Utilizador JOIN Paciente AS P on Utilizador.ID = P.ID WHERE Nome LIKE %s", (filter, ))


        if patients is not None:
            for (ID, Nome, Num_Utente) in patients:
                params_dict["patients"].append(
                    {"name": Nome, "niss": Num_Utente, "id": {"_id": ID}, "last_appointment": "17/4/2019"})
                params_dict["total_patients"] += 1
        else:
            flash("No results found")
            return redirect(url_for("doctor_dashboard_patients"))

        patients.close()

    return render_template('doctor-dashboard-patients.html', params=params_dict)

@app.route('/doctor-dashboard/patients/<_id>')
def doctor_dashboard_patient_info(_id):
    #TODO: Melhorar página HTML
    _id = int(_id)

    # Get personal info about the patient
    cursor = db.cursor()
    cursor.execute("SELECT Num_Utente, Nome, Email, Tel, Idade, Morada, NIF FROM Paciente JOIN Utilizador U "
                   "on Paciente.ID = U.ID WHERE Paciente.ID = %s", (_id, ))

    patient = cursor.fetchone()

    params_dict = {"name": patient[1]  , "niss": patient[0], "email": patient[2], "tel": patient[3], "age":patient[4], "address": patient[5],
                   "nif": patient[6], "illnesses": []}

    # Get diseases info, if they exist

    diseases = []

    cursor.execute("SELECT Nome FROM Diagnostico JOIN Doenca D "
                   "on D.Codigo = Diagnostico.Cod_Doenca WHERE Id_Pac = %s", (_id, ))

    for Nome in cursor:
        diseases.append(Nome)

    if len(diseases) == 0:
        params_dict["illnesses"].append("This patient has no diseases")
    else:
        params_dict["illnesses"] = diseases


    cursor.close()

    return render_template('doctor-dashboard-patient-info.html', params=params_dict)


@app.route('/doctor-dashboard/appointments', methods=["GET", "POST"])
def doctor_dashboard_appointments():
    # here there will be a cursor.execute( "SELECT * FROM appointments WHERE doctor_id = {id_of_authenticated_doctor}")
    # which will return an iterator
    # TODO: Search bar query: Check to see if the flash message is appearing when searching for query with no results, once Sessions have been implemented
    # TODO: Replace with commented version once login of autenthicated users is setup
    """
    params_dict = {"appointments": []}
    for result in iterator:
        params_dict["appointments"].append({"date": result.date, "...": ..., ...})

    params_dict["total_appointments"] = len(params_dict["appointments"]

    """

    params_dict = {"appointments":[], "total_appointments": 0}

    if request.method == "GET":
        '''
        doctor_id = session["user_ID"]

        appointments = db.cursor()
        appointments.execute("SELECT * FROM Consulta WHERE ID_Med = %s", (doctor_id, ))

        for (Num_Cons, ID_Med, ID_Pac, Cod_Esp, Data) in appointments:
            # Separar Data da Hora
            dia, hora = str(Data).split(" ")

            # Buscar info do Nome do Paciente à tabela de Utilizadores
            cursor = db.cursor()

            cursor.execute("SELECT Nome FROM Paciente JOIN Utilizador U on U.ID = Paciente.ID WHERE U.ID=%s", (ID_Pac,))
            name = cursor.fetchone()

            # Buscar info do nome da especialidade

            cursor.execute("SELECT Nome FROM Especialidade WHERE Codigo=%s", (Cod_Esp,))
            especialidade = cursor.fetchone()

            params_dict["appointments"].append(
                {"date": dia, "hour": hora, "id": {"_id": Num_Cons}, "specialty": especialidade[0], "patient": name[0]})
            params_dict["total_appointments"] += 1

            cursor.close()
            
        appointments.close()
        '''

        # For testing purposes:
        appointments = db.cursor()
        appointments.execute("SELECT * FROM Consulta")

        for (Num_Cons, ID_Med, ID_Pac, Cod_Esp, Data) in appointments:
            # Separar Data da Hora
            dia, hora = str(Data).split(" ")

            # Buscar info do Nome do Paciente à tabela de Utilizadores
            cursor = db.cursor()

            cursor.execute("SELECT Nome FROM Paciente JOIN Utilizador U on U.ID = Paciente.ID WHERE U.ID=%s", (ID_Pac, ))
            name = cursor.fetchone()

            # Buscar info do nome da especialidade

            cursor.execute("SELECT Nome FROM Especialidade WHERE Codigo=%s", (Cod_Esp, ))
            especialidade = cursor.fetchone()

            params_dict["appointments"].append({"date": dia, "hour": hora, "id": {"_id": Num_Cons}, "specialty": especialidade[0], "patient": name[0]})
            params_dict["total_appointments"] += 1

            cursor.close()


        appointments.close()

    elif request.method == "POST":
        filter = "%" + request.form["filter"] + "%"

        patients = db.cursor()
        patients.execute("select Utilizador.ID, Nome from Utilizador JOIN Paciente AS P on Utilizador.ID = P.ID WHERE Nome LIKE %s",
            (filter,))

        if patients is not None:
            for (ID, Nome) in patients:
                appointments = db.cursor()

                appointments.execute("SELECT Num_Cons, Nome, Data FROM Consulta JOIN Especialidade "
                                     "ON Consulta.Cod_Esp = Especialidade.Codigo "
                                     "WHERE ID_Pac=%s", (ID, ))

                for (Num_Cons, Especialidade, Data) in appointments:
                    # Separar Data da Hora
                    dia, hora = str(Data).split(" ")

                    params_dict["appointments"].append(
                        {"date": dia, "hour": hora, "id": {"_id": Num_Cons}, "specialty": Especialidade, "patient": Nome})
                    params_dict["total_appointments"] += 1

                appointments.close()
        else:
            flash("No results found for your search query")
            return redirect(url_for("doctor_dashboard_patients"))

        patients.close()


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
    print(_id)
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


@app.route('/doctor-dashboard/prescriptions/form', methods=('GET', 'POST'))
def doctor_dashboard_prescription_form():
    if request.method == "POST":
        appointment_id = request.form.get('appointmentID')
        medic_id = request.form.get("medicID")
        patient_name = request.form.get("patientName")
        pharma_multiselect = request.form.getlist('pharmaceutical_multiselect')

        print(appointment_id)
        print(medic_id)
        print(patient_name)
        print(pharma_multiselect)
        flash("Prescription created sucessfully.", 'success')
        return redirect(url_for('doctor_dashboard_prescription_form'))

    params_dict = {"pharmaceuticals": ["Bruffen", "Paracetamol", "Anti-depressive", "Bruffen", "Paracetamol",
                                       "Anti-depressive"]}
    return render_template('doctor-dashboard-prescription-form.html', params=params_dict)

# end of doctor-dashboard


# admin dashboard


@app.route('/admin', methods=('GET', 'POST'))
def admin():

    cursor = db.cursor()
    cursor.execute("SELECT * FROM Medico LEFT JOIN Utilizador ON Medico.ID = Utilizador.ID")
    for medico in cursor.fetchall():
        print(medico)

    if request.method == "POST":
        form_id = request.args.get('form_id', 1, type=int)
        if form_id == 1:
            print(request.form)
            print(request.args.get('form_id', 1, type=int))
            return redirect(url_for('admin'))
        elif form_id == 2:
            print(request.form)
            print(request.args.get('form_id', 1, type=int))
            return redirect(url_for('admin'))
        elif form_id == 3:
            print(request.form)
            print(request.args.get('form_id', 1, type=int))
            return redirect(url_for('admin'))

    return render_template('admin-dashboard.html', params={})


def get_patient_info(patient_id):
    return "hello"


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
