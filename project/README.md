# TODO LIST

## Homepage and Login

Data do Site: 20/11
### Homepage
- Página de contactos disponivel a partir da homepage
- Discuss if newsletter is good idea to keep or not 
- Discuss what to keep from the existing footer links   

### Review Page
- Lista de Reviews antigas
- Form para escrever nova review

## Pacient Pages
### Main Page
- Fazer hardcode da data para mostrar upcoming exams, como nas páginas do médico
- Backend 

HTML:
- Mudar logo da uni para logo usado nas páginas do Médico
- Prescrição: Input para receber código da Prescrição. Se tiver válido, apresentar informação
- Mudar 'Exams' para 'Appointments'
- Upcoming APpointments - Apagar os 3 pontos das opções

### Make an Appointment
- Acrescentar input de data

- Backend

### Contacts
- Ideias?

## Admin Dashboard Page
- Make the html page


## Doctor Pages
### Medic Dashboard Page
- Make backend connections
- Hard-code a Date to show info about Today's Appointments, Next Appointment...
    - Populate the DB with info about appointments and prescriptions for this date
- Prescriptions made today
  - Associate with appointment's date
HTML:
- Logout button
- Logo redirect to dashboard
- Details about next appointment redirect to appointment
- Today's Exams -> Today's Appointments
- Apresentar mensagem "Bem-vindo {nome}"

## Patients e Patients/Id
- Rework HTML do patients/id

## Appointments e Appointments/id
- Adaptar backend do Patients
- Rework HTML do appointments/id

## Prescriptions
- Adaptar backend do Patients
- Rework HTML do appointments/id
- Fazer backend do forms

## Running the app with a virtual environment
```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```