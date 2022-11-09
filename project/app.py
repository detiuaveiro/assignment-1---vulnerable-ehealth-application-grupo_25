from flask import Flask, render_template

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


@app.route('/logged')       #mudar isto futuramente
def logged():
    return render_template('logged.html')


@app.route('/create-acc')
def createacc():
    return render_template('createacc.html')


@app.route('/doctor-dashboard')
def doctor_dashboard():
    return render_template('doctor-dashboard.html')


@app.route('/doctor-dashboard/patients')
def doctor_dashboard_patients():
    return render_template('doctor-dashboard-patients.html')


@app.route('/doctor-dashboard/appointments')
def doctor_dashboard_appointments():
    return render_template('doctor-dashboard-appointments.html')


@app.route('/doctor-dashboard/prescriptions')
def doctor_dashboard_prescriptions():
    return render_template('doctor-dashboard-prescription.html')

if __name__ == '__main__':
    app.run(use_reloader=True)


