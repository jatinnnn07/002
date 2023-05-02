import sqlite3

def create_connection(db_file):
    """Create a connection to SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f'Successfully connected to database: {sqlite3.version}')
    except sqlite3.Error as e:
        print(e)
    return conn

def create_patient(conn, patient):
    """Insert new patient into the patients table"""
    sql = '''INSERT INTO patients(name, dob, gender, address, phone, email)
             VALUES(?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, patient)
    conn.commit()
    return cur.lastrowid

def main():
    database = 'hospital.db'
    conn = create_connection(database)
    
    with conn:
        # example patient data
        patient = ('John Smith', '1990-01-01', 'Male', '123 Main St', '555-555-5555', 'john.smith@example.com')
        patient_id = create_patient(conn, patient)
        print(f'Patient record created with ID: {patient_id}')

if __name__ == '__main__':
    main()
