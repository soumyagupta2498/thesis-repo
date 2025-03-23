import logging

logging.basicConfig(filename='patient_log.txt', level=logging.INFO)

class Patient:
    def __init__(self, name, ssn, diagnosis):
        self.name = name
        self.ssn = ssn
        self.diagnosis = diagnosis

def store_patient_record(patient):
    with open("records.txt", "a") as file:
        file.write(f"{patient.name},{patient.ssn},{patient.diagnosis}\n")

def send_data_to_third_party(patient):
    print(f"Sending {patient.name}'s data to third-party provider...")

def log_activity(patient):
    logging.info(f"Accessed patient: {patient.name}, SSN: {patient.ssn}")

p1 = Patient("Alice Johnson", "123-45-6789", "Diabetes")
store_patient_record(p1)
log_activity(p1)
send_data_to_third_party(p1)
print("Operation completed.")
