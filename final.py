from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Define the patient data model
class Patient:
    def __init__(self, id, name, dob, gender, address, phone, email):
        self.id = id
        self.name = name
        self.dob = dob
        self.gender = gender
        self.address = address
        self.phone = phone
        self.email = email

# Define the API endpoints
@app.route('/patients', methods=['GET', 'POST'])
def patients():
    # Create a connection to the database
    conn = sqlite3.connect('hospital.db')
    cur = conn.cursor()

    if request.method == 'GET':
        # Retrieve all patients from the database
        cur.execute('SELECT * FROM patients')
        rows = cur.fetchall()

        # Convert the patient records into a list of Patient objects
        patients = []
        for row in rows:
            patient = Patient(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            patients.append(patient.__dict__)

        # Return the list of patients as a JSON response
        return jsonify(patients)

    elif request.method == 'POST':
        # Insert a new patient into the database
        patient = Patient(None, request.json['name'], request.json['dob'], request.json['gender'], request.json['address'], request.json['phone'], request.json['email'])
        sql = 'INSERT INTO patients(name, dob, gender, address, phone, email) VALUES (?, ?, ?, ?, ?, ?)'
        cur.execute(sql, (patient.name, patient.dob, patient.gender, patient.address, patient.phone, patient.email))
        conn.commit()
        patient.id = cur.lastrowid

        # Return the newly created patient as a JSON response
        return jsonify(patient.__dict__)

    else:
        return 'Invalid request'

if __name__ == '__main__':
    app.run(debug=True)
