# TODO LIST

## Homepage and Login
## Homepage
- Página de contactos disponivel a partir da homepage
- Discuss if newsletter is good idea to keep or not 
- Discuss what to keep from the existing footer links

## Contact Form Page
- Make the html page

## Pacient Pages
### Main Page
- Fazer hardcode da data para mostrar upcoming exams, como nas páginas do médico 
- Backend 

HTML:
- Mudar logo da uni para logo usado nas páginas do Médico - DONE
- Prescrição: Input para receber código da Prescrição. Se tiver válido, apresentar informação 
- Mudar 'Exams' para 'Appointments' - DONE
- Upcoming APpointments - Apagar os 3 pontos das opções - DONE

### Make an Appointment
- Acrescentar input de data - DONE 

- Backend

### Contacts
- Ideias? - ?

## Admin Dashboard Page
- Make the html page - DONE


## Doctor Pages
### Medic Dashboard Page
- Make backend connections DONE
- Hard-code a Date to show info about Today's Appointments, Next Appointment... DONE
    - Populate the DB with info about appointments and prescriptions for this date
- Prescriptions made today DONE
  - Associate with appointment's date DONE
HTML:
- Logout button DONE
- Logo redirect to dashboard DONE
- Details about next appointment redirect to appointment (should be details about patient, because appointment is not yet made) DONE
- Today's Exams -> Today's Appointments DONE
- Apresentar mensagem "Bem-vindo {nome}"  DONE

## Patients e Patients/Id
- Rework HTML do patients/id DONE
- When flash error, update actual data not hardcoded

## Appointments e Appointments/id
- Adaptar backend do Patients DONE
- Rework HTML do appointments/id DONE
- Mudar o placeholder do search

## Prescriptions
- Adaptar backend do Patients DONE
- Rework HTML do appointments/id DONE
- Fazer backend do forms, atualizar para processar as listas

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