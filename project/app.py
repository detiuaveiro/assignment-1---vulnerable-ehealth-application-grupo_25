from flask import Flask, render_template, request, flash, redirect, url_for, session
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


db = mysql.connector.connect(
    host="localhost",
    #port=3307,
    #user="root",
    #password="1904",
    get_warnings=True,
    user="daniel",
    password="8495",
    database="eHealthCorp",
    #user="bruna",
    #password="12345678",
    #database="sio_db"
)

'''
Contas:
-> Médico: afgomes@mail.pt pass: 1234
-> Paciente: art.afo@ua.pt pass: 1904
'''

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

        # There are no warnings
        warnings = cursor.fetchwarnings()
        print(warnings)

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

@app.route('/contactdoctor')
def contactdoctor():
    return render_template('contact-doctor.html')

@app.route('/create-acc', methods=['GET', 'POST'])
def createacc():
    if request.method == 'POST':
        form_input = {
            "firstname": request.form['firstname'],
            "lastname": request.form['lastname'],
            "email": request.form['email'],
            "nutente": request.form['nutente'],
            "nif": request.form['nif'],
            "tel": request.form['tel'],
            "morada": request.form['morada'],
            "password": request.form['psw'],
            "confirm_password": request.form['pswc']
        }

        for key, value in form_input.items():
            if value == "":
                form_input[key] = None

        if form_input["password"] != form_input["confirm_password"]:
            flash("Passwords don't match")
            return redirect(url_for('createacc'))
        
        cursor = db.cursor()

        cursor.execute('''
            INSERT INTO Utilizador (Nome, Email, Tel, Password, Idade, Morada, NIF)
            VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            , (form_input["firstname"] + " "+ form_input["lastname"], form_input["email"], form_input["tel"], form_input["password"], None, form_input["morada"], form_input["nif"]))
        
        cursor.execute('''
            INSERT INTO Paciente (ID, Num_Utente)
            VALUES (%s, %s)'''
            , (cursor.lastrowid, form_input["nutente"]))

        db.commit()
        
        return redirect(url_for('login'))

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
    """
    params_dict = {"patients": []}
    for result in iterator:
        params_dict["patients"].append({"name": result.name, "...": ..., ...})

    params_dict["total_patients"] = len(params_dict["patients"]

    """
    params_dict = {"patients": [], "total_patients": 0}
    doctor_id = session["user_id"]

    if request.method == "GET":
        cursor = db.cursor()
        cursor.execute("SELECT ID_Pac FROM Med_Pac WHERE ID_Med=%s", (doctor_id,))

        patients_id = cursor.fetchall()

        for (ID_Pac) in patients_id:
            cursor.execute("SELECT U.ID, Nome, Num_Utente "
                                 "FROM (Paciente JOIN Utilizador U on U.ID = Paciente.ID) "
                                 "WHERE U.ID=%s LIMIT 1", tuple(ID_Pac))

            patient = cursor.fetchone()

            cursor.execute("SELECT Data FROM Consulta WHERE ID_Pac=%s ORDER BY Data LIMIT 1", tuple(ID_Pac))

            data = cursor.fetchone()

            if data is not None:
                last_appointment = data[0]
            else:
                last_appointment = "Nenhum"

            # Adicionar info ao params_dict
            params_dict["patients"].append({"name": patient[1], "niss": patient[-1], "id": {"_id": ID_Pac[0]}, "last_appointment": last_appointment})
            params_dict["total_patients"] += 1

        cursor.close()

    elif request.method == "POST":
        filter = "%" + request.form["filter"] + "%"

        cursor = db.cursor()
        cursor.execute("SELECT ID_Pac, Nome, Num_Utente FROM Med_Pac JOIN Pac_User_View ON ID_Pac=ID WHERE ID_Med=%s AND Nome LIKE %s", (doctor_id, filter, ))

        patients = cursor.fetchall()

        if len(patients) > 0:
            for (ID_Pac, Nome, Num_Utente) in patients:
                params_dict["patients"].append(
                    {"name": Nome, "niss": Num_Utente, "id": {"_id": ID_Pac[0]}, "last_appointment": "17/4/2019"})
                params_dict["total_patients"] += 1
        else:
            flash("No results found")
            return redirect(url_for("doctor_dashboard_patients"))

        cursor.close()

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
        diseases.append(Nome[0])

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

    params_dict = {"appointments": [], "total_appointments": 0}
    doctor_id = session["user_id"]

    if request.method == "GET":
        cursor = db.cursor()
        cursor.execute("SELECT Num_Cons, ID_Pac, Nome, Data "
                       "FROM Consulta JOIN Especialidade ON Cod_Esp=Especialidade.Codigo "
                       "WHERE ID_Med = %s", (doctor_id, ))

        consultas = cursor.fetchall()

        for (Num_Cons, ID_Pac, Especialidade, Data) in consultas:
            # Separar Data da Hora
            dia, hora = str(Data).split(" ")

            # Buscar info do Nome do Paciente à tabela de Utilizadores
            cursor = db.cursor()

            cursor.execute("SELECT Nome FROM Paciente JOIN Utilizador U on U.ID = Paciente.ID WHERE U.ID=%s", (ID_Pac,))
            name = cursor.fetchone()

            # Adicionar info ao params_dict
            params_dict["appointments"].append(
                {"date": dia, "hour": hora, "id": {"_id": Num_Cons}, "specialty": Especialidade, "patient": name[0]})
            params_dict["total_appointments"] += 1

            cursor.close()
    elif request.method == "POST":
        filter = "%" + request.form["filter"] + "%"

        cursor = db.cursor()
        cursor.execute("SELECT Num_Cons, ID_Pac, Nome, Data "
                       "FROM Consulta JOIN Especialidade ON Cod_Esp=Especialidade.Codigo "
                       "WHERE ID_Med = %s", (doctor_id,))

        consultas = cursor.fetchall()

        for (Num_Cons, ID_Pac, Especialidade, Data) in consultas:
            # Separar Data da Hora
            dia, hora = str(Data).split(" ")

            # Buscar info do Nome do Paciente à tabela de Utilizadores
            cursor = db.cursor()

            cursor.execute("SELECT Nome FROM Paciente JOIN Utilizador U on U.ID = Paciente.ID WHERE U.ID=%s AND Nome LIKE %s ", (ID_Pac, filter, ))
            patient = cursor.fetchall()

            if len(patient) > 0:
                for (Nome) in patient:
                    # Adicionar info ao params_dict
                    params_dict["appointments"].append(
                        {"date": dia, "hour": hora, "id": {"_id": Num_Cons}, "specialty": Especialidade,
                         "patient": Nome[0]})
                    params_dict["total_appointments"] += 1
            else:
                flash("No results found")
                return redirect(url_for("doctor_dashboard_appointments"))

                cursor.close()


    return render_template('doctor-dashboard-appointments.html', params=params_dict)


@app.route('/doctor-dashboard/appointments/<_id>')
def doctor_dashboard_appointment_info(_id):
    # TODO: Melhorar página HTML
    _id = int(_id)

    cursor = db.cursor()
    cursor.execute("SELECT Num_Cons, ID_Med, ID_Pac, Nome, Data "
                   "FROM Consulta JOIN Especialidade ON Cod_Esp=Especialidade.Codigo WHERE Num_Cons = %s", (_id, ))

    dados_consulta = cursor.fetchone()

    ## Buscar nome do Médico e do Paciente

    cursor.execute("SELECT Nome FROM Pac_User_View WHERE ID=%s", (dados_consulta[2], ))
    nome_paciente = cursor.fetchone()

    cursor.execute("SELECT Nome FROM Med_User_View WHERE ID=%s", (dados_consulta[1],))
    nome_medico = cursor.fetchone()

    # Separar Data da Hora
    dia, hora = str(dados_consulta[-1]).split(" ")


    params_dict = {"date": dia, "hour": hora, "specialty": dados_consulta[3],
                   "patient": nome_paciente[0], "doctor": nome_medico[0]}

    return render_template('doctor-dashboard-appointment-info.html', params=params_dict)


@app.route('/doctor-dashboard/prescriptions')
def doctor_dashboard_prescriptions():
    params_dict = {"prescriptions": [], "total_prescriptions": 0}
    doctor_id = session["user_id"]
    prescriptions_code = set()

    if request.method == "GET":
        cursor = db.cursor()
        cursor.execute("SELECT Code, Data, ID_Pac FROM Prescricao JOIN Consulta C "
                       "ON Prescricao.Num_Consulta = C.Num_Cons "
                       "WHERE C.ID_Med=%s", (doctor_id,))

        prescriptions = cursor.fetchall()

        for (Code, Data, ID_Pac) in prescriptions:
            if Code in prescriptions_code:
                continue

            prescriptions_code.add(Code)

            # Separar Data da Hora
            dia, hora = str(Data).split(" ")

            # Buscar info do Nome do Paciente à tabela de Utilizadores
            cursor = db.cursor()

            cursor.execute("SELECT Nome FROM Paciente JOIN Utilizador U on U.ID = Paciente.ID WHERE U.ID=%s", (ID_Pac,))
            name = cursor.fetchone()


            # Adicionar info ao params_dict
            params_dict["prescriptions"].append(
                {"date": dia, "id": {"_id": Code}, "patient": name[0]})
            params_dict["total_prescriptions"] += 1

            cursor.close()

    return render_template('doctor-dashboard-prescription.html', params=params_dict)


@app.route('/doctor-dashboard/prescriptions/<_id>')
def doctor_dashboard_prescription_info(_id):
    print(_id)
    pharmaceuticals = []

    cursor = db.cursor()
    cursor.execute("SELECT Code, ID_Pac, Data, Cod_Medic FROM Prescricao JOIN Consulta C on C.Num_Cons = Prescricao.Num_Consulta WHERE Code = %s", (_id, ))

    prescription = cursor.fetchall()

    for (Code, ID_Pac, Data, Cod_Medic) in prescription:
        # Buscar o nome do Paciente
        print(Cod_Medic)

        cursor.execute("SELECT Nome FROM Pac_User_View WHERE ID = %s", (ID_Pac, ))
        name = cursor.fetchone()

        # Buscar os Faramacêuticos
        cursor.execute("SELECT Nome FROM Medicamento WHERE Codigo = %s", (Cod_Medic, ))
        pharma = cursor.fetchone()

        print(pharma)
        pharmaceuticals.append(pharma[0])


    params_dict = {"date": Data,
                   "patient": name[0], "id": _id,
                   "pharmaceuticals": pharmaceuticals}

    cursor.close()
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

    elif request.method == "GET":
        pharmaceuticals = []
        cursor = db.cursor()
        cursor.execute("SELECT Nome FROM Medicamento")

        pharma = cursor.fetchall()

        for name in pharma:
            pharmaceuticals.append(name[0])

        params_dict = {"pharmaceuticals": pharmaceuticals}
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
