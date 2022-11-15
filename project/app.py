from flask import Flask, render_template, request, flash, redirect, url_for, session
import random
import string
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'


db = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="1904",
    get_warnings=True,
    #user="daniel",
    #password="8495",
    database="eHealthCorp",
    #user="bruna",
    #password="12345678",
    #database="sio_db"
    #user='andre',
    #password='Password123#@!',
    #database='db1',
)

'''
Contas:
-> Médico: afgomes@mail.pt pass: 1234
-> Paciente: art.afo@ua.pt pass: 1904
'''

todays_date = ("2022-11-15 00:00:00", "2022-11-15 23:59:59")

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


@app.route('/logout')
def logout():
    if session.get('user_id') is not None:
        session.pop('user_id', None)
        session.pop('email', None)

    return redirect(url_for('index'))


@app.route('/contactform', methods=['GET', 'POST'])
def contactform():
    if request.method == 'POST':
        pass
    
    if request.method == 'GET':
        pass

    return render_template('contactform.html')


@app.route('/logged', methods=['GET', 'POST'])
def logged():
    if session.get('user_id') is None:
        return redirect(url_for('login'))
    
    if request.method == 'GET':
        ctx = {
            'user_id': session.get('user_id'),
            'pacient_info': [],
            'appointments': [],
        } 

        cursor = db.cursor()
        cursor.execute("SELECT * FROM  Pac_User_View WHERE ID = %s", (session.get('user_id'),))
        ctx['pacient_info'] = cursor.fetchone()

        cursor.execute("SELECT * FROM Consulta WHERE ID_Pac = %s AND Data >= %s", (session.get('user_id'), todays_date[0]))
        appointment_db_data = cursor.fetchall() 
        print(appointment_db_data)
        for appointment in appointment_db_data:
            medic_id = appointment[1]
            cursor.execute("SELECT Nome, Cod_Esp FROM Med_User_View WHERE ID = %s", (medic_id,))
            medic_data = cursor.fetchone()
            nome_medico = medic_data[0]
            cod_esp = medic_data[1]
            cursor.execute("SELECT Nome FROM Especialidade WHERE Codigo = %s", (cod_esp,))
            especialidade = cursor.fetchone()[0]
            datetime = str(appointment[4])
            data = datetime.split(" ")[0]
            horas = datetime.split(" ")[1]
            ctx['appointments'].append((nome_medico, especialidade, data, horas))

        cursor.close()

        return render_template('logged.html', ctx=ctx)

    return render_template('logged.html')

@app.route('/patient-prescription-details', methods=['GET', 'POST'])
def patient_prescription_details():
    if request.method == 'POST':
        prescription_code = request.form["prescription_code"]
        pharmaceuticals = []

        cursor = db.cursor()
        cursor.execute("SELECT Code, ID_Pac, Data, Cod_Medic FROM Prescricao JOIN Consulta C on C.Num_Cons = Prescricao.Num_Consulta WHERE Code = %s", (prescription_code, ))

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
                    "patient": name[0], "id": prescription_code,
                    "pharmaceuticals": pharmaceuticals} 
        
        return render_template('patient-prescription-details.html', params=params_dict)

@app.route('/patient_exam_details', methods=['GET', 'POST'])
def patient_exam_details():
    if request.method == 'POST':
        exam_code = request.form["exam_code"]
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Analise WHERE Codigo = %s", (exam_code, ))
        exam = cursor.fetchone()
        print(exam)
        params_dict = {"date": exam[1],
                    "patient": exam[2], "id": exam_code,
                    "exam_type": exam[3], "result": exam[4]} 
        
        return render_template('patient-exam-details.html', params=params_dict)

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

        # Verificar se o email já existe
        cursor = db.cursor()
        cursor.execute("SELECT Email FROM Utilizador WHERE Email = %s", (form_input["email"],))
        email_data = cursor.fetchone()
        if email_data is not None:
            flash("Email already exists")
            return redirect(url_for('createacc'))
        

        for key, value in form_input.items():
            if value == "":
                form_input[key] = None

        if form_input["password"] != form_input["confirm_password"]:
            flash("Passwords don't match")
            return redirect(url_for('createacc'))
        

        cursor.execute('''
            INSERT INTO Utilizador (Nome, Email, Tel, Password, Idade, Morada, NIF)
            VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            , (form_input["firstname"] + " "+ form_input["lastname"], form_input["email"], form_input["tel"], form_input["password"], None, form_input["morada"], form_input["nif"]))
        
        cursor.execute('''
            INSERT INTO Paciente (ID, Num_Utente)
            VALUES (%s, %s)'''
            , (cursor.lastrowid, form_input["nutente"]))

        db.commit()
        cursor.close()
        
        return redirect(url_for('login'))

    return render_template('createacc.html')

@app.route('/appointment', methods=["GET", "POST"])
def appointment():
    if request.method == "GET":
        params_dict = dict()
        params_dict['doctors'] = []

        cursor = db.cursor()

        cursor.execute("SELECT ID, Med_User_View.Nome, Especialidade.Nome FROM Med_User_View JOIN Especialidade ON Cod_Esp = Codigo")

        doctors = cursor.fetchall()

        for (ID, Doc_Name, Especialidade) in doctors:
            params_dict['doctors'].append({
                "ID": ID, "Name": Doc_Name, "Specialty": Especialidade
            })

        cursor.close()
    elif request.method == "POST":
        id_medico = request.form.get('doctorSelect')
        date = request.form.get("date")
        hour = request.form.get("hour")

        if not id_medico or not date or not hour:
            flash("Please fill all the fields")
            return redirect(url_for("appointment"))
        else:
            cursor = db.cursor()

            pacient_id = session["user_id"]
            query_date = str(date) + " " +  str(hour)

            cursor.execute("SELECT Cod_Esp FROM Medico JOIN Especialidade E on E.Codigo = Medico.Cod_Esp WHERE ID=%s", (id_medico, ))
            cod_esp = cursor.fetchone()

            cursor.execute('''
                        INSERT INTO Consulta (ID_Med, ID_Pac, Cod_Esp, Data) 
                        VALUES (%s, %s, %s, %s)''',
                           (id_medico, pacient_id, cod_esp[0], query_date))
            db.commit()
            cursor.close()
            flash("Appointment scheduled successfully!")
            return redirect(url_for("logged"))


    return render_template('user-appointment.html', params=params_dict)


# doctor-dashboard
@app.route('/doctor-dashboard')
def doctor_dashboard():
    params_dict = {}
    doctor_id = session["user_id"]
    cursor = db.cursor()

    cursor.execute("SELECT Nome FROM Utilizador WHERE ID=%s", (doctor_id,))
    params_dict['doctor_name'] = cursor.fetchone()[0]

    cursor.execute("SELECT Num_Cons, ID_Pac, Nome, Data "
                   "FROM Consulta JOIN Especialidade ON Cod_Esp=Especialidade.Codigo "
                   "WHERE ID_Med = %s AND Data BETWEEN %s AND %s", (doctor_id, todays_date[0], todays_date[1]))

    consultas = cursor.fetchall()
    params_dict['total_todays_appointments'] = 0
    params_dict['todays_appointments'] = []

    for (Num_Cons, ID_Pac, Especialidade, Data) in consultas:
        # Separar Data da Hora
        dia, hora = str(Data).split(" ")

        # Buscar info do Nome do Paciente à tabela de Utilizadores
        cursor.execute("SELECT Nome FROM Paciente JOIN Utilizador U on U.ID = Paciente.ID WHERE U.ID=%s", (ID_Pac,))
        name = cursor.fetchone()

        # Adicionar info ao params_dict
        params_dict["todays_appointments"].append(
            {"date": dia, "hour": hora, "patient": name[0], 'patient_id': ID_Pac, 'num_appointment': Num_Cons})
        params_dict['total_todays_appointments'] += 1
        params_dict['todays_appointments'].sort(key=lambda x: x['hour'])

    cursor.execute("SELECT Code, Data, ID_Pac FROM Prescricao JOIN Consulta C "
                   "ON Prescricao.Num_Consulta = C.Num_Cons "
                   "WHERE C.ID_Med=%s AND Data BETWEEN %s AND %s", (doctor_id, todays_date[0], todays_date[1], ))

    prescriptions = cursor.fetchall()
    params_dict["prescriptions"] = []
    prescriptions_code = []
    for (Code, Data, ID_Pac) in prescriptions:
        if Code in prescriptions_code:
            continue

        # Separar Data da Hora
        dia, hora = str(Data).split(" ")

        # Buscar info do Nome do Paciente à tabela de Utilizadores
        cursor.execute("SELECT Nome FROM Paciente JOIN Utilizador U on U.ID = Paciente.ID WHERE U.ID=%s", (ID_Pac,))
        name = cursor.fetchone()

        # Adicionar info ao params_dict
        prescriptions_code.append(Code)
        params_dict["prescriptions"].append(
            {"date": dia, "id": Code, "patient": name[0]})

    cursor.close()

    return render_template('doctor-dashboard.html', params=params_dict)


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
                    {"name": Nome, "niss": Num_Utente, "id": {"_id": ID_Pac}, "last_appointment": "17/4/2019"})
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
        cursor.execute(
            "SELECT ID_Pac, Nome FROM Med_Pac JOIN Pac_User_View ON ID_Pac=ID WHERE ID_Med=%s AND Nome LIKE %s",
            (doctor_id, filter,))

        pacientes = cursor.fetchall()

        if len(pacientes) == 0:
            cursor.close()
            flash("No results found")
            return redirect(url_for("doctor_dashboard_appointments"))

        for (ID_Pac, Nome) in pacientes:
            cursor.execute("SELECT Num_Cons, Nome, Data "
                           "FROM Consulta JOIN Especialidade ON Cod_Esp=Especialidade.Codigo "
                           "WHERE ID_Med = %s AND ID_Pac=%s", (doctor_id, ID_Pac, ))

            consultas = cursor.fetchall()

            if len(consultas) > 0:
                for (Num_Cons, Especialidade, Data) in consultas:
                    # Separar Data da Hora
                    dia, hora = str(Data).split(" ")

                    # Adicionar info ao params_dict
                    params_dict["appointments"].append(
                        {"date": dia, "hour": hora, "id": {"_id": Num_Cons}, "specialty": Especialidade,
                         "patient": Nome})
                    params_dict["total_appointments"] += 1
            else:
                cursor.close()
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
        id_medico = session["user_id"]
        id_medicamentos = request.form.getlist('pharmaceutical_multiselect')
        prescription_code = get_random_code()

        if not appointment_id or not id_medicamentos:
            flash("Please fill all the fields")
            return redirect(url_for("doctor_dashboard_prescription_form"))
        else:
            cursor = db.cursor()
            for id_medicamento in id_medicamentos:
                cursor.execute('''
                    INSERT INTO Prescricao (Cod_Medic, Num_Consulta, Id_Med, Code) 
                    VALUES (%s, %s, %s, %s)''', 
                    (id_medicamento, appointment_id, id_medico, prescription_code))
            db.commit()
            cursor.close()
            flash("Prescription created successfully")
            return redirect(url_for("doctor_dashboard_prescriptions"))

    elif request.method == "GET":
        params_dict = dict()
        params_dict['pharmaceuticals'] = []
        params_dict['appointment_ids'] = []
        doctor_id = session["user_id"]
        cursor = db.cursor()

        cursor.execute("SELECT Codigo, Nome FROM Medicamento")

        pharmas = cursor.fetchall()

        for pharma in pharmas:
            params_dict['pharmaceuticals'].append((pharma[0], pharma[1]))

        cursor.execute("SELECT Num_Cons, ID_Pac, Nome, Data "
                       "FROM Consulta JOIN Especialidade ON Cod_Esp=Especialidade.Codigo "
                       "WHERE ID_Med = %s", (doctor_id,))

        consultas = cursor.fetchall()
        cursor.close()

        for consulta in consultas:
            params_dict['appointment_ids'].append(consulta[0])

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


@app.route('/reviews', methods=["GET", "POST"])
def reviews():
    params_dict = {"reviews": [], "total_reviews": 0}
    if request.method == "POST":
        name = request.form.get('name')
        review = request.form.get('review')
        print(name, review)

        if not name or not review:
            flash("Please fill all the fields")
            return redirect(url_for("reviews"))
        else:
            cursor = db.cursor()
            cursor.execute('''
                INSERT INTO Comentario (Autor, Texto) 
                VALUES (%s, %s)''',
                           (name, review))
            db.commit()
            cursor.close()
            flash("Prescription created successfully")
            return redirect(url_for("reviews"))

    elif request.method == "GET":
        params_dict['reviews'] = []

        cursor = db.cursor()
        cursor.execute("SELECT * FROM Comentario")
        reviews = cursor.fetchall()
        

        for (ID, Autor, Texto, Data) in reviews:
            params_dict["reviews"].append({"date": Data,
                           "author": Autor, "id": ID,
                           "text": Texto})
            params_dict["total_reviews"] += 1


    return render_template('reviews.html', params=params_dict)


def get_random_code():
    """Generate a random string"""
    str = string.ascii_uppercase
    return ''.join(random.choice(str) for i in range(3)).join(random.choice(string.digits) for i in range(2))


if __name__ == '__main__':
    app.run(use_reloader=True, debug=True)
